#!/usr/bin/env python3
"""
Module: task_04_flask.py

This module implements a simple RESTful API using Flask.

The API provides the following endpoints:
- GET /              : Returns a welcome message.
- GET /status        : Returns API status.
- GET /data          : Returns a list of all usernames.
- GET /users/<username> : Returns user details for a given username.
- POST /add_user     : Adds a new user via JSON payload.

Example of valid JSON for POST /add_user:
{
    "username": "alice",
    "name": "Alice",
    "age": 25,
    "city": "San Francisco"
}
"""

from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}

@app.route("/")
def home():
    """
    Root endpoint. Returns a welcome message.
    """
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    """
    Status check endpoint. Returns "OK".
    """
    return "OK"


@app.route("/data")
def get_username():
    """
    Returns a list of all usernames stored in memory.
    """
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    """
    Returns detailed info of a user if found.
    If not, returns a 404 error message.
    """
    if username not in users:
        return jsonify({"error": "User not found"})
    user_data = users[username].copy()
    user_data["username"] = username
    return jsonify(user_data)


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Adds a user via POST request with JSON body.
    Requires 'username' field.
    Returns confirmation with user data or 400 error if missing.
    """
    data = request.get_json()

    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    users[username] = {
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    user_data = users[username].copy()
    user_data["username"] = username

    return jsonify({"message": "User added", "user": user_data}), 201


if __name__ == "__main__":
    app.run()
