# FastAPI Learning Notes

## Lecture 1 — FastAPI Basics

FastAPI is a Python web framework used to build backend applications and APIs.

### Creating a FastAPI Application

First, import FastAPI:

```python
from fastapi import FastAPI
```

Create the FastAPI application:

```python
app = FastAPI()
```

`FastAPI()` creates the FastAPI application.

### Routes / Endpoints

A route defines a URL path that a client can access.

```python
@app.get("/")
def home():
    return "Welcome to FastAPI"
```

`@app.get("/")` creates a GET endpoint at `/`.

When a client sends a GET request to `/`, FastAPI runs the `home()` function and returns its response.

### Multiple Routes

We can create multiple endpoints in the same FastAPI application:

```python
@app.get("/contact")
def contact():
    return "Contact Us anytime you want, Thank you!"
```

The application can now respond to:

* `GET /` → `Welcome to FastAPI`
* `GET /contact` → `Contact Us anytime you want, Thank you!`

### Basic Flow

Client → HTTP Request → FastAPI Route → Python Function → Response

**Key idea:** FastAPI maps an incoming HTTP request to a Python function and returns the function's result as the response.
