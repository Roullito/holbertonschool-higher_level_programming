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

---

## 📄 Task 1: Consume data from an API using `curl`

### 📅 Objective

By the end of this task, you should be able to:

* Use `curl` to send `GET` and `POST` requests to an API
* View and interpret HTTP response headers
* Understand the structure of requests sent via the command line

---

### 🚪 Tools Used

* `curl`
* API endpoint: `https://jsonplaceholder.typicode.com/posts`

---

### 📊 Observations

* `curl https://jsonplaceholder.typicode.com/posts`

  * Sends a default `GET` request
  * Returns a JSON array of post objects
  * Each object contains: `userId`, `id`, `title`, `body`

* `curl -I https://jsonplaceholder.typicode.com/posts`

  * Returns only the HTTP headers
  * Includes important headers like `Content-Type`, `Server`, `X-RateLimit-Remaining`, `Cache-Control`, etc.

* `curl -X POST -d "title=hello&body=test_content&userId=1" https://jsonplaceholder.typicode.com/posts`

  * Sends a `POST` request with URL-encoded data
  * The response is a JSON object containing the submitted data and a generated `id`

---

### 🔄 Summary

Using `curl`, you can:

* Interact with APIs via the command line
* Simulate `GET`, `POST`, `PUT`, or `DELETE` requests
* Send data using `-d`
* View raw HTTP headers using `-I`

This is a powerful tool for testing, debugging, and learning API interaction without needing a browser or frontend.

---

## 🧰 Tasks 2 to 5 – API Coding Exercises

The following tasks involve writing and running actual Python code to interact with or implement RESTful APIs. Each task is located in the `restful-api` directory and has its own file.

### 🔹 Task 2: Consume an API with Python (`requests`)
- File: `task_02_requests.py`
- Objective: Fetch posts from an API using `requests`, print titles, and save them to a CSV file using the `csv` module.

### 🔹 Task 3: Develop an API using `http.server`
- File: `task_03_http_server.py`
- Objective: Create a basic HTTP server with custom GET routes, including `/`, `/data`, `/status`, and handle 404 errors with JSON responses.

### 🔹 Task 4: Build a Flask-based API
- File: `task_04_flask.py`
- Objective: Use Flask to define routes (`/`, `/status`, `/data`, `/users/<username>`, `/add_user`), store user data in memory, handle GET/POST, and return JSON responses.

### 🔹 Task 5: Secure your API
- File: `task_05_basic_security.py`
- Objective: Implement both Basic Auth and JWT authentication using Flask extensions. Protect routes and restrict access based on user roles (e.g., admin vs. user).

Please refer to each script file for full implementation and usage examples.

---

## 📂 Repository Info

```
GitHub repository: holbertonschool-higher_level_programming
Directory: restful-api
```
