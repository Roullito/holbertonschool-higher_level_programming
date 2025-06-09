# 📡 RESTful API – Holberton School

## 🎡 Project: RESTful API – Novice Level

**By Javier Valenzani – Holberton School**

---

## 🎯 Learning Objectives

This project aims to give you practical and theoretical knowledge of RESTful APIs, covering everything from consumption to development and security:

* Understand the basics of HTTP/HTTPS
* Interact with an API using `curl` (command line)
* Consume APIs in Python (`requests` library)
* Create simple APIs using `http.server`
* Develop scalable APIs with Flask
* Secure APIs using Basic Auth and JWT
* Document APIs with OpenAPI standards

---

## 🌐 Task 0: Basics of HTTP/HTTPS

### 📅 Objective

By the end of this task, you should be able to:

* Differentiate between HTTP and HTTPS
* Understand the structure of HTTP requests and responses
* Recognize and explain common HTTP methods and status codes

---

### 🔐 HTTP vs HTTPS

| Criteria     | HTTP                        | HTTPS                                     |
| ------------ | --------------------------- | ----------------------------------------- |
| Security     | ❌ No encryption             | ✅ Encrypted via SSL/TLS                   |
| Default Port | 80                          | 443                                       |
| Usage        | For non-sensitive data      | For sensitive data (e.g., login, banking) |
| Protocol     | HyperText Transfer Protocol | HyperText Transfer Protocol Secure        |

**Summary**: HTTPS is HTTP with an added security layer (SSL/TLS). It ensures that data is encrypted, protecting users from eavesdropping and tampering.

---

### 🪧 Structure of an HTTP Request and Response

#### 📬 Request Example

```http
GET /index.html HTTP/1.1
Host: example.com
Accept: text/html
User-Agent: Mozilla/5.0
```

#### 🛤️ Response Example

```http
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 3057
```

---

### ⚙️ Common HTTP Methods

| Method | Description                  | Example Use Case                     |
| ------ | ---------------------------- | ------------------------------------ |
| GET    | Retrieve a resource          | Fetching a web page or list of items |
| POST   | Create a new resource        | Submitting a registration form       |
| PUT    | Replace an existing resource | Replacing user profile data          |
| PATCH  | Partially update a resource  | Updating only the username           |
| DELETE | Delete a resource            | Removing a post or user account      |

---

### 📲 Common HTTP Status Codes

| Code | Meaning               | Example Scenario                              |
| ---- | --------------------- | --------------------------------------------- |
| 200  | OK                    | Request succeeded and data returned           |
| 201  | Created               | New resource was created successfully         |
| 204  | No Content            | Action was successful but no content returned |
| 400  | Bad Request           | Malformed request or invalid input            |
| 401  | Unauthorized          | Missing or invalid authentication credentials |
| 403  | Forbidden             | Authenticated but lacks permission            |
| 404  | Not Found             | Resource does not exist                       |
| 500  | Internal Server Error | Generic server error                          |

---

### 🔀 HTTP Communication Flow Diagram

```text
    [CLIENT]                                        [SERVER]

        | 1. Sends HTTP(S) Request                 |
        | ---------------------------------------> |
        | GET /users HTTP/1.1                      |
        | Host: api.example.com                    |
        | Accept: application/json                 |
        |                                          |
        | 2. Server Processes Request              |
        | 3. Sends HTTP Response                   |
        | <--------------------------------------- |
        | HTTP/1.1 200 OK                          |
        | Content-Type: application/json           |
```

## 📂 Repository Info

```
GitHub repository: holbertonschool-higher_level_programming
Directory: restful-api
```
