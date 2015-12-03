"""
Health check, Login, and for Flask-HTTPAuth hooks.

"""

from flask import (
    Blueprint,
    request,
    jsonify,
    abort,
    current_app
)
import os
from ..extensions import auth, db


blueprint = Blueprint(
    'misc',
    __name__)


@blueprint.route('/health')
def health():
    # TODO check DB
    return jsonify({'msg': 'success', 'status_code': 200}), 200

@auth.get_password
def get_password(username):
    """
    Return the password for *username*.

    """
    if not username:
        abort(401)

    if not username == os.environ.get('HTTP_BASICAUTH_USERNAME'):
        abort(401)

    current_app.logger.debug('Retrieving password for %s' % username)
    return os.environ.get('HTTP_BASICAUTH_PASSWORD')
