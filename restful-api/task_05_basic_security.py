#!/usr/bin/python3
"""
Flask API with user authentication (Basic & JWT) and role-based access control.

Endpoints:
- GET /basic-protected     → Basic Auth protected route
- POST /login              → JWT login with credentials
- GET /jwt-protected       → JWT token protected route
- GET /admin-only          → JWT token + role check (admin only)

Requirements:
- Flask
- Flask-HTTPAuth
- Flask-JWT-Extended
- Werkzeug (for password hashing)
"""

from flask import Flask, request, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token,
    get_jwt_identity, jwt_required
)

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "123456"
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """
    Basic Auth: verify user credentials.
    """
    if username in users:
        hashed_password = users[username]['password']
        if check_password_hash(hashed_password, password):
            return username
    return None


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_auth():
    """
    Protected route using HTTP Basic Auth.
    """
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """
    Login with JSON body, returns JWT token if valid credentials.
    JSON:
    {
        "username": "user1",
        "password": "password"
    }
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if username in users:
        hashed_password = users[username]['password']
        if check_password_hash(hashed_password, password):
            token = create_access_token(identity=username)
            return jsonify({"access_token": token}), 200
    return jsonify({"error": "Invalid credentials"}), 401


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def protected():
    """
    Protected route using JWT token.
    """
    return jsonify({"message": "JWT Auth: Access Granted"}), 200


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin():
    """
    Admin-only route. Requires JWT token and 'admin' role.
    """
    username = get_jwt_identity()
    role = users[username]["role"]
    if role == "admin":
        return jsonify({"message": "Admin Access: Granted"}), 200
    else:
        return jsonify({"error": "Admin access required"}), 403


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run(debug=True)
