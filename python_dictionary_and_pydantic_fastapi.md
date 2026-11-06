# Dictionaries and Pydantic in FastAPI

## Quick revision

- **Dictionary (`dict`)**: stores key-value data. `product["name"]` reads a
  value; `product.get("name")` is handy when the key might be missing.
- **Pydantic model**: describes the fields and types an API expects. FastAPI
  validates request data against it. Bad data gets a `422` response.
- `model_dump()` turns a Pydantic object into a dictionary.

## Example

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Product(BaseModel):
    name: str
    price: float


products = []


@app.post("/products")
def add_product(product: Product):
    data = product.model_dump()
    products.append(data)
    return data


@app.get("/products")
def get_products():
    return products
```

Send `{"name": "Camera", "price": 499.99}` to `POST /products`.
FastAPI turns the JSON into a `Product`; `model_dump()` gives the dictionary
stored in `products`.

**Remember:** Pydantic checks the shape; dictionaries hold the data.
