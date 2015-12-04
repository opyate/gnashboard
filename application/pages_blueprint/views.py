from flask import (
    Blueprint,
)
from ..extensions import auth
from ..models.page import Page


blueprint = Blueprint(
    'pages',
    __name__,
    template_folder='templates')


@blueprint.route('/pages')
@blueprint.route('/pages/<string:name>')
def index(name=None):
    if name:
        page = Page.query \
                   .filter_by(name=name) \
                   .order_by(Page.created_ts.desc()) \
                   .limit(1).first()
        if page:
            return page.html, 200
    return "<p>No page here</p>", 404
