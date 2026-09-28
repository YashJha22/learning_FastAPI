# REST API Notes

## 1. What is an API?

An API (Application Programming Interface) is a communication interface
that allows one software system to communicate with another software system.

Example:

Android App → API → Backend → Database

The API defines how the Android app can communicate with the backend.

---
## 2. What is REST?

REST stands for Representational State Transfer. It is a way of designing APIs so that communication between the client and server is simple and organized.

REST treats the data of an application as resources.

For example:

/users
/products
/orders

Each resource has its own URL, and different operations can be performed on these resources using HTTP methods.

````md
## 3. HTTP Methods

HTTP methods tell the server what action the client wants to perform on a resource.

```text
HTTP Method → What do I want to do?
URL         → Which resource?
````

The main HTTP methods used in REST APIs are:

* `GET` → Read/retrieve data
* `POST` → Create new data
* `PUT` → Replace existing data
* `PATCH` → Partially update existing data
* `DELETE` → Delete data

### GET

`GET` is used to retrieve data from the server.

Example:

```http
GET /products
```

This means:

* `GET` → retrieve/read data
* `/products` → the products resource

To retrieve one specific product:

```http
GET /products/5
```

Here `/products/5` identifies product with ID `5`.



