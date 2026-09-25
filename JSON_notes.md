````markdown
# JSON Notes

## What is JSON?

**JSON (JavaScript Object Notation)** is a standard format used to represent and exchange structured data between applications.

Example:

```json
{
  "name": "Yash",
  "age": 20,
  "student": true
}
````

---

## Key-Value Pairs

JSON uses **key-value pairs**.

```json
{
  "name": "Yash",
  "age": 20
}
```

* `"name"` → key
* `"Yash"` → value
* `"age"` → key
* `20` → value

---

## JSON Data Types

JSON supports:

* String
* Number
* Boolean
* Null
* Array
* Object

### String

```json
{
  "name": "Yash"
}
```

### Number

```json
{
  "age": 20
}
```

### Boolean

```json
{
  "student": true
}
```

### Null

Represents the absence of a value.

```json
{
  "phone": null
}
```

### Array

Stores multiple values.

```json
{
  "skills": ["Java", "Kotlin", "Python"]
}
```

### Object

Contains key-value pairs and can be nested.

```json
{
  "name": "Yash",
  "address": {
    "city": "Patna",
    "country": "India"
  }
}
```

---

## JSON Syntax Rules

### Double Quotes

Keys and strings use **double quotes**.

```json
{
  "name": "Yash"
}
```

### No Trailing Comma

Incorrect:

```json
{
  "name": "Yash",
  "age": 20,
}
```

Correct:

```json
{
  "name": "Yash",
  "age": 20
}
```

---

## JSON in HTTP

JSON is commonly used as the **body of HTTP requests and responses**.

Example:

```http
POST /users
Content-Type: application/json
```

Body:

```json
{
  "name": "Yash",
  "age": 20
}
```

`Content-Type: application/json` tells the server that the body contains JSON.

---

## HTTP vs JSON

**HTTP** = communication protocol

**JSON** = data format

```text
HTTP → how applications communicate
JSON → how the data is structured
```

---

## JSON vs Python Dictionary

They look similar but are different.

Python dictionary:

```python
user = {
    "name": "Yash",
    "age": 20
}
```

JSON:

```json
{
  "name": "Yash",
  "age": 20
}
```

A Python dictionary is a Python data structure.

JSON is a standard format for exchanging data between applications.

---

## Key Takeaway

> **JSON is a standard format for structuring and exchanging data between applications.**

```
```
