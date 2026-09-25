
```markdown
# 🌐 HTTP & HTTPS Fundamentals

---

## 1. Client-Server Model

Web communication operates on a request-response cycle between two parties:

* **Client:** The initiator (e.g., Browser, Mobile App, Postman, `curl`). Sends an HTTP Request.
* **Server:** The provider (e.g., Nginx, Apache, FastAPI backend). Processes the request and sends back an HTTP Response.

```text
[ Client / App ]  ─── ( HTTP Request ) ───►  [ Web Server ]
[ Client / App ]  ◄─── ( HTTP Response ) ───  [ Web Server ]

```

---

## 2. HTTP vs. HTTPS

| Feature | HTTP (Hypertext Transfer Protocol) | HTTPS (HTTP Secure) |
| --- | --- | --- |
| **Data Protocol** | Plain Text | Encrypted via **TLS/SSL** |
| **Default Port** | `80` | `443` |
| **Security Risk** | High (Vulnerable to packet sniffing & MITM attacks) | Secure (Provides Confidentiality, Integrity, & Authentication) |
| **Certificates** | None required | Requires an SSL/TLS Certificate signed by a CA |

---

## 3. Resource Identifiers: URI vs. URL vs. URN

* **URI (Uniform Resource Identifier):** The overarching category used to identify any resource.
* **URL (Uniform Resource Locator):** Identifies **WHERE** a resource is located and **HOW** to access it.
* *Example:* `https://example.com:443/products/item?id=42#reviews`


* **URN (Uniform Resource Name):** Identifies a resource by a **NAME** in a specific namespace, regardless of where it lives.
* *Example:* `urn:isbn:0451450523` (Identifies a book by its ISBN).



```text
                  ┌───────────────────────────────┐
                  │             URI               │
                  │ (Uniform Resource Identifier) │
                  └───────────────┬───────────────┘
                                  │
          ┌───────────────────────┴───────────────────────┐
          ▼                                               ▼
  ┌───────────────┐                               ┌───────────────┐
  │      URL      │                               │      URN      │
  │  (Locator)    │                               │    (Name)     │
  └───────────────┘                               └───────────────┘

```

---

## 4. HTTP Request Body (Payload)

The **HTTP Body** holds the actual content being transferred (JSON, Form Data, HTML, Images).

* `GET`, `HEAD`, `DELETE`, and `OPTIONS` generally **do not** send a request body.
* `POST`, `PUT`, and `PATCH` use the request body to send payload data to the server.

### Example JSON Payload:

```http
POST /api/users HTTP/1.1
Host: api.example.com
Content-Type: application/json
Content-Length: 48

{
  "name": "Alex",
  "role": "developer"
}

```

---

## 5. HTTP Methods (Verbs)

HTTP Methods define the operations performed on a server resource. They map directly to **CRUD** database operations.

| Method | CRUD Action | Request Body? | Safe? | Idempotent? | Description |
| --- | --- | --- | --- | --- | --- |
| **`GET`** | **Read** | No | **Yes** | **Yes** | Fetches data without modifying server state. |
| **`POST`** | **Create** | Yes | No | No | Creates a new resource on the server. |
| **`PUT`** | **Update** | Yes | No | **Yes** | **Completely replaces** a resource (or creates it if missing). |
| **`PATCH`** | **Update** | Yes | No | No | **Partially updates** specific fields of an existing resource. |
| **`DELETE`** | **Delete** | Optional | No | **Yes** | Removes a specified resource. |
| **`HEAD`** | **Read** | No | **Yes** | **Yes** | Same as `GET`, but returns headers only (no body). |
| **`OPTIONS`** | **Utility** | No | **Yes** | **Yes** | Returns allowed HTTP methods (used in CORS preflights). |

> **Definitions:**
> * **Safe:** Executing the request does not change the server's state (Read-only).
> * **Idempotent:** Making the exact same request 1 time or 100 times leaves the server in the exact same state.
> 
> 

---

## 6. HTTP Status Codes

Status codes are 3-digit integers returned by the server to indicate the result of a request.

### 🟢 1xx - Informational

* **`100 Continue`**: Server received initial headers; client can continue sending the body.
* **`101 Switching Protocols`**: Upgrading connection protocol (e.g., HTTP to WebSocket).

### 🟢 2xx - Success

* **`200 OK`**: Standard successful response.
* **`201 Created`**: Resource successfully created (`POST`/`PUT`).
* **`204 No Content`**: Request succeeded, but no body is returned (e.g., after `DELETE`).

### 🟡 3xx - Redirection

* **`301 Moved Permanently`**: Resource URL has permanently changed.
* **`302 Found`**: Temporary redirect.
* **`304 Not Modified`**: Client cached copy is still valid (saves bandwidth).

### 🟠 4xx - Client Error

* **`400 Bad Request`**: Malformed payload or missing required parameters.
* **`401 Unauthorized`**: Missing or invalid authentication token/credentials.
* **`403 Forbidden`**: Client is authenticated but lacks access permissions.
* **`404 Not Found`**: Target URL or resource does not exist.
* **`409 Conflict`**: Request state conflicts with server data (e.g., duplicate email).
* **`429 Too Many Requests`**: Rate limit exceeded.

### 🔴 5xx - Server Error

* **`500 Internal Server Error`**: Unhandled exception or backend crash.
* **`502 Bad Gateway`**: Edge proxy received an invalid response from upstream app server.
* **`503 Service Unavailable`**: Server is down for maintenance or overloaded.
* **`504 Gateway Timeout`**: Upstream server failed to respond in time.

---

## 7. Modern Security: TLS / SSL

HTTPS relies on **TLS (Transport Layer Security)**, which replaced the outdated **SSL (Secure Sockets Layer)**.

### The 4 Pillars of TLS

1. **Encryption:** Obfuscates data in transit.
2. **Authentication:** Verifies server identity using SSL/TLS X.509 Certificates.
3. **Integrity:** Uses MACs to ensure data isn't altered during transfer.
4. **Handshake:** Dynamically generates encrypted session keys between client and server.

---

## 8. Quick Mental Model (The Restaurant Analogy)

| HTTP Concept | Real-World Restaurant Analogy |
| --- | --- |
| **Client** | You (the customer ordering food) |
| **Server** | The kitchen staff preparing your meal |
| **HTTP** | Delivery driver using an open bag (unencrypted) |
| **HTTPS** | Delivery driver using a locked safe box (encrypted) |
| **`GET`** | *"Bring me the menu."* |
| **`POST`** | *"Place a new order."* |
| **`PUT`** | *"Cancel my whole meal and replace it with this new set."* |
| **`PATCH`** | *"Keep my order, just change diet coke to regular coke."* |
| **`DELETE`** | *"Cancel my order entirely."* |
| **`200 OK`** | *"Here is your food!"* |
| **`404 Not Found`** | *"That dish is not on our menu."* |
| **`500 Error`** | *"The kitchen stove caught fire!"* |

