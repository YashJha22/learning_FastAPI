# Python Dictionaries and Pydantic Objects in FastAPI

FastAPI receives and returns JSON. It uses Python dictionaries and Pydantic
models to work with that data.

## Python Dictionary

A dictionary stores data as key-value pairs. It is useful for flexible data,
such as records kept temporarily in memory.

```python
product_data = {
    "id": 1,
    "title": "Camera",
    "price": 499.99,
    "count": 5,
}

print(product_data["title"])  # Camera
product_data["count"] = 4
```

Use `.get()` when a key may not exist; indexing a missing key raises
`KeyError`.

```python
discount = product_data.get("discount", 0)
```

## Pydantic Model

A Pydantic model defines the expected fields and validates their values.
FastAPI uses it to validate request bodies and document the API.

```python
from pydantic import BaseModel, Field


class Product(BaseModel):
    id: int
    title: str
    price: float = Field(ge=0)
    count: int = Field(ge=0)
```

Build a model from a dictionary with `model_validate()`. Invalid data raises
`ValidationError`.

```python
product = Product.model_validate(product_data)
print(product.title)
```

Convert a model back to a normal Python dictionary with `model_dump()`.

```python
product_dict = product.model_dump()
```

## Use Both in a FastAPI App

This example accepts a validated `Product` request body, stores it as a
dictionary, and returns product data validated by the response model.

```python
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Product(BaseModel):
    id: int
    title: str
    price: float = Field(ge=0)
    count: int = Field(ge=0)


products: list[dict[str, int | str | float]] = []


@app.post("/products", response_model=Product)
def create_product(product: Product) -> dict[str, int | str | float]:
    product_data = product.model_dump()
    products.append(product_data)
    return product_data


@app.get("/products", response_model=list[Product])
def get_products() -> list[dict[str, int | str | float]]:
    return products
```

For `POST /products`, send this JSON request body:

```json
{
  "id": 1,
  "title": "Camera",
  "price": 499.99,
  "count": 5
}
```

FastAPI parses the JSON into a `Product` object and Pydantic checks its fields.
For example, a negative price fails validation and FastAPI responds with
`422 Unprocessable Entity`. The endpoint converts the validated model to a
dictionary for storage. `response_model=Product` (or
`response_model=list[Product]`) validates and documents the returned data.

## When to Use Each

- Use a **Pydantic model** for structured request or response data with known
  fields and validation rules.
- Use a **dictionary** for flexible key-value data or simple in-memory
  storage.
- A common flow is: JSON request → Pydantic model → `model_dump()` dictionary
  → response validated by a Pydantic response model.
