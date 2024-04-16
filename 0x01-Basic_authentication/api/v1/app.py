#!/usr/bin/env python3
''' basic cofe for Flask '''
from flask import Flask, jsonify
from api.v1.views.index import app_views


app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(401)
def unauthorized(error) -> str:
    ''' handles error 401 for unauthorized req '''
    response = jsonify({'error': 'Unauthorized'})
    response.status_code = 401
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
