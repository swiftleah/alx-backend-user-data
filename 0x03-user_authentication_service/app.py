#!/usr/bin/env python3
''' code for flask application '''
from flask import Flask, request, jsonify
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/")
def flaskapp() -> str:
    ''' flaskapp route '''
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=["POST"], strict_slashes=False)
def users() -> str:
    ''' endpoint to register a user '''
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")