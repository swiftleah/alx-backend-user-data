#!/usr/bin/env python3
""" Module of Index views"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def status() -> str:
    """Return the status of the API"""
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """Return the number of each objects"""
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)


@app_views.route("/unauthorized/", strict_slashes=False)
def unauthorized() -> str:
    """ GET /api/v1/unauthorized"""
    abort(401)


@app_views.route("/forbidden/", strict_slashes=False)
def forbidden() -> str:
    """ GET /api/v1/forbidden"""
    abort(403)
