#!/usr/bin/env python3
"""
Simple RESTful API using Flask
"""

from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!", 200, {"Content-Type": "text/plain"}

@app.route("/status")
def status():
    return "OK", 200, {"Content-Type": "text/plain"}

@app.route("/data")
def get_username():
    return jsonify(list(users.keys()))

@app.route("/users/<username>")
def get_user(username):
    if username not in users:
        return jsonify({"error": "User not found"})
    user_data = users[username].copy()
    user_data["username"] = username
    return jsonify(user_data)

@app.route("/add_user", methods=["POST"])
def add_user():
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
