#!/usr/bin/env python3
''' basic code for Flask application '''
from flask import abort, Blueprint


app_views = Blueprint('app_views', __name__)


@app_views.route('/api/v1/unauthorized', methods=['GET'])
def unauthorized() -> None:
    ''' defines route /api/v1/unauthorized
    when GET req is made -> returns 401 error '''
    abort(401)
