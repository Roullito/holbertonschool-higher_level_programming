#!/usr/bin/env python3
"""
Simple RESTful API using Flask.

This module implements a basic REST API with Flask that allows:
- Welcome message at root endpoint
- Status check endpoint
- User data management (create, read, list)
- In-memory storage using dictionary

Author: Holberton School Exercise
"""

from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route("/", methods=["GET"])
def home():
    """
    Handle GET requests to the root endpoint.

    Returns:
        str: Welcome message for the Flask API.
    """
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    """
    Handle GET requests to check API status.

    Returns:
        str: Status message indicating the API is operational.
    """
    return "OK"


@app.route("/data", methods=["GET"])
def data():
    """
    Handle GET requests to retrieve all usernames.

    Returns:
        Response: JSON response containing a list of all usernames
                 stored in the API.
    """
    return jsonify(list(users.keys()))


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """
    Handle GET requests to retrieve a specific user by username.

    Args:
        username (str): The username of the user to retrieve.

    Returns:
        Response: JSON response containing the user data if found,
                 or an error message if the user doesn't exist.
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"})


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Handle POST requests to add a new user to the API.

    Expected JSON payload:
        {
            "username": str (required),
            "name": str (optional),
            "age": int (optional),
            "city": str (optional)
        }

    Returns:
        Response: JSON response with success message and user data
                 if successful (status 201), or error message
                 if username is missing (status 400).
    """
    data = request.get_json()

    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    """
    Run the Flask development server when script is executed directly.

    The server will start on localhost:5000 by default.
    Debug mode is disabled for production-like behavior.
    """
    app.run()
