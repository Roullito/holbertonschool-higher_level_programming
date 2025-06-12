#!/usr/bin/python3
"""Flask API server with user management capabilities"""
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route("/")
def home():
    """Root endpoint - Returns welcome message"""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Data endpoint - Returns list of all usernames"""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Status endpoint - Returns API status"""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """User endpoint - Get user details by username

    Args:
        username (str): Username to lookup

    Returns:
        JSON: User data or error message
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add user endpoint - Creates a new user

    Expected JSON body:
    {
        "username": "john_doe",
        "other_fields": "values"
    }

    Returns:
        JSON: Success message and user data or error
    """
    user_data = request.get_json()
    username = user_data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
