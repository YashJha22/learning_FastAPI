# REST API Notes

## 1. What is an API?

An API (Application Programming Interface) is a communication interface
that allows one software system to communicate with another software system.

Example:

Android App → API → Backend → Database

The API defines how the Android app can communicate with the backend.
The API defines the rules and format for how the client communicates with the server.

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

````md
### POST

`POST` is used to create new data on the server.

Example:

```http
POST /products
````

This means:

* `POST` → create new data
* `/products` → the products resource

The client can send the new product data in the request body:

```json
{
  "name": "Laptop",
  "price": 50000
}
```

The server then creates the product and usually returns the newly created resource.

### POST

`POST` is used to create new data on the server.

Example:

```http
POST /products
````

This means:

* `POST` → create new data
* `/products` → the products resource

The client can send the new product data in the request body:

```json
{
  "name": "Laptop",
  "price": 50000
}
```

The server then creates the product and usually returns the newly created resource.



## PUT

```md
### PUT

`PUT` is used to replace an existing resource with new data.

Example:

```http
PUT /products/5
```

This means:

- `PUT` → replace the existing data
- `/products/5` → the product with ID `5`

The client sends the new data in the request body:

```json
{
  "name": "Laptop Pro",
  "price": 70000
}
```

The server updates product `5` using the provided data.

`PUT` generally represents a complete replacement of the resource.
'''




