# Python Type Hints

## 1. What Are Type Hints?

Type hints indicate the expected types of variables, function parameters, and return values. They make code easier to understand and help tools detect potential mistakes.

Python does not generally enforce type hints at runtime by itself.

```python
name: str = "Task"
count: int = 5
is_completed: bool = False
```

## 2. Type Hints in Functions

Parameter annotations describe expected inputs. The return annotation describes the expected return type.

```python
def calculate_total(price: float, quantity: int) -> float:
    return price * quantity
```

`price: float` annotates the parameter, while `-> float` annotates the return value.

## 3. Common Types

- `str`: text
- `int`: integers
- `float`: decimal numbers
- `bool`: Boolean values
- `list[str]`: a list of strings
- `dict[str, int]`: a dictionary with string keys and integer values
- `None`: absence of a return value

## 4. Optional Values

A value that can be either a string or `None` can be annotated as:

```python
description: str | None = None
```

This is different from saying a field is optional in every context. Whether a value must be supplied also depends on its default and, when using Pydantic, the model's field definition.

## 5. Type Hints in FastAPI

FastAPI uses Python annotations to understand endpoint parameters, validate certain inputs, and generate API documentation.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    return {"task_id": task_id}
```

Here, `task_id: int` tells FastAPI to interpret the path parameter as an integer. An invalid integer input results in a validation error.

## 6. Type Hints vs. Pydantic

Type hints describe expected types. They do not, by themselves, validate arbitrary incoming JSON at runtime.

Pydantic models build on type annotations to validate structured data.

For example, a future task request schema can declare fields such as a task title and completion status. Pydantic will then validate incoming request data against that schema.

## Key Takeaways

- Type hints improve readability and tooling support.
- Function annotations describe inputs and return values.
- `str | None` allows a value to be a string or `None`.
- FastAPI uses annotations when processing endpoint parameters.
- Pydantic will be the next topic for validating request bodies.
