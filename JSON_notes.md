````markdown
# JSON

## What is JSON?

**JSON (JavaScript Object Notation)** is a lightweight text-based format used to represent and exchange structured data between programs.

In simple words:

> **JSON is a common format that allows different programs to understand and exchange data.**

Example:

```json
{
  "name": "Yash",
  "age": 20
}
````

---

## JSON Structure

JSON mainly uses **key-value pairs**.

```json
{
  "name": "Yash",
  "age": 20
}
```

Here:

```text
"name" → key
"Yash" → value

"age" → key
20     → value
```

The key describes the data, and the value is the actual data.

---

## JSON Syntax Rules

### 1. Use double quotes

JSON uses **double quotes** for keys and strings.

Correct:

```json
{
  "name": "Yash"
}
```

Incorrect:

```json
{
  'name': 'Yash'
}
```

### 2. Separate key-value pairs with commas

```json
{
  "name": "Yash",
  "age": 20,
  "student": true
}
```

### 3. Don't use a trailing comma

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

## JSON Data Types

JSON supports these main data types:

* String
* Number
* Boolean
* Null
* Array
* Object

### String

Used for text.

```json
{
  "name": "Yash"
}
```

Strings use double quotes.

---

### Number

Used for numbers.

```json
{
  "age": 20,
  "height": 175.5
}
```

Numbers don't need quotes.

```json
"age": 20
```

is a number.

```json
"age": "20"
```

is a string.

---

### Boolean

Boolean values are:

```text
true
false
```

Example:

```json
{
  "isStudent": true
}
```

`true` and `false` are not strings.

---

### Null

`null` means there is no value.

```json
{
  "phone": null
}
```

For example, a user may not have provided their phone number yet.

---

### Array

An array stores multiple values.

```json
{
  "skills": ["Java", "Kotlin", "Python"]
}
```

Arrays use square brackets:

```text
[ ]
```

Arrays can contain different types of JSON values.

Example:

```json
{
  "marks": [85, 90, 78]
}
```

Arrays can also contain objects:

```json
{
  "students": [
    {
      "name": "Yash",
      "age": 20
    },
    {
      "name": "Rahul",
      "age": 21
    }
  ]
}
```

---

### Object

An object contains related key-value pairs.

```json
{
  "name": "Yash",
  "age": 20
}
```

Objects use:

```text
{ }
```

Objects can also be nested inside other objects.

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

## Complete Example

```json
{
  "id": 101,
  "name": "Yash",
  "age": 20,
  "student": true,
  "phone": null,
  "skills": ["Java", "Kotlin", "Python"],
  "address": {
    "city": "Patna",
    "country": "India"
  }
}
```

Types:

```text
id       → Number
name     → String
age      → Number
student  → Boolean
phone    → Null
skills   → Array
address  → Object
```

---

# JSON in HTTP

JSON is commonly used as the **body of HTTP requests and responses**.

Example:

```http
POST /users
Content-Type: application/json
```

The header:

```text
Content-Type: application/json
```

tells the server that the request body contains JSON.

The body:

```json
{
  "name": "Yash",
  "age": 20
}
```

The flow:

```text
Android App
     |
     | HTTP Request
     | JSON Body
     ↓
  FastAPI
     |
     | HTTP Response
     | JSON Body
     ↓
Android App
```

---

# HTTP vs JSON

They are different things.

### HTTP

HTTP is the **protocol used for communication** between a client and server.

### JSON

JSON is the **format used to structure the data** being exchanged.

Think:

```text
HTTP = how the data is communicated
JSON = how the data is structured
```

Example:

```text
HTTP Request
│
├── Method → POST
├── URL → /users
├── Header → Content-Type: application/json
│
└── Body
      ↓
     JSON
      ↓
{
  "name": "Yash",
  "age": 20
}
```

---

# JSON vs Python Dictionary

They look similar but are not the same thing.

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

A Python dictionary is a **Python data structure**.

JSON is a **standard data format**.

FastAPI/Pydantic can process incoming JSON and convert the data into Python objects that your code can work with.

---

# How to Explain JSON

If someone asks **"What is JSON?"**, you should be able to say:

> **JSON stands for JavaScript Object Notation. It's a lightweight text-based format used to represent and exchange structured data between programs. It uses key-value pairs and supports strings, numbers, booleans, null, arrays, and objects. APIs commonly use JSON as the data format in HTTP request and response bodies.**

Example:

```json
{
  "name": "Yash",
  "age": 20,
  "skills": ["Java", "Python"]
}
```

Here:

* `"name"` is a key
* `"Yash"` is its value
* `20` is a number
* `skills` is an array

---

## Key Takeaway

> **JSON is a structured, readable data format that allows different applications to exchange data consistently.**

```
```
