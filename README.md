# rest-api-with-flask-
# 👨‍💻 Flask REST API - User Management

This is a simple REST API built with Flask to manage user data. It supports basic CRUD operations: **Create**, **Read**, **Update**, and **Delete**.

## 🚀 Features

- Get all users
- Get a single user by ID
- Add a new user
- Update an existing user
- Delete a user

## 🛠️ Tech Stack

- Python 3
- Flask
📡 API Endpoints
✅ GET all users
bash
Copy
Edit
GET /users
✅ GET a user by ID
bash
Copy
Edit
GET /users/<id>
✅ POST a new user
bash
Copy
Edit
POST /users
Sample JSON:
json
Copy
Edit
{
  "id": 3,
  "name": "Charlie",
  "email": "charlie@example.com"
}
✅ PUT (update) a user
bash
Copy
Edit
PUT /users/<id>
Sample JSON:
json
Copy
Edit
{
  "name": "New Name",
  "email": "new@example.com"
}
✅ DELETE a user
bash
Copy
Edit
DELETE /users/<id>
🧪 Testing
You can use Postman or cURL to test the API endpoints.




