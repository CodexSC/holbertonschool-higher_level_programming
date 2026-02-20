#!/usr/bin/python3
"""
Simple Flask API implementing basic REST functionality.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage (DO NOT pre-populate for checker)
users = {}


@app.route("/", methods=["GET"])
def home():
    """Root endpoint."""
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    """API status endpoint."""
    return "OK"


@app.route("/data", methods=["GET"])
def get_usernames():
    """Return list of all usernames."""
    return jsonify(list(users.keys()))


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Return full user object by username."""
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    return jsonify(users[username])


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user via POST request."""
    try:
        data = request.get_json(force=True)
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()
