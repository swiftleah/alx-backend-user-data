#!/usr/bin/env python3
from flask import abort, jsonify, request
from api.v1.views import app_views
from models.user import User

@app_views.route('/users/me', methods=['GET'], strict_slashes=False)
def get_me():
    """Get current user."""
    if request.current_user is None:
        abort(404)
    return jsonify(request.current_user.to_dict()), 200
