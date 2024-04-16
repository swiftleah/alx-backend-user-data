#!/usr/bin/env python3
''' basic code for Flask '''
from flask import Flask, jsonify, request, abort
from api.v1.views.index import app_views
from api.v1.auth.auth import Auth
from api.v1.auth.basic_auth import BasicAuth
from os import getenv
import os


app = Flask(__name__)
app.register_blueprint(app_views)


auth = None


auth_type = os.getenv('AUTH_TYPE')


if auth_type == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
else:
    auth = Auth()


@app.before_request
def before_request():
    ''' authenticates a user before processing a request '''
    if auth:
        excluded_paths = [
                '/api/v1/status/',
                '/api/v1/unauthorized/',
                '/api/v1/forbidden/',
        ]
        if auth.require_auth(request.path, excluded_paths):
            auth_header = auth.authorization_header(request)
            user = auth.current_user(request)
            if auth_header is None:
                abort(401)
            if user is None:
                abort(403)


@app.errorhandler(401)
def unauthorized(error) -> str:
    ''' handles error 401 for unauthorized req '''
    response = jsonify({"error": "Unauthorized"})
    response.status_code = 401
    return response


@app.errorhandler(403)
def forbidden(error) -> str:
    ''' handles error 403 - no access '''
    response = jsonify({"error": "Forbidden"})
    response.status_code = 403
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
