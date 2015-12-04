from flask import (
    Blueprint,
)
from ..extensions import auth, db
from ..models.page import Page


blueprint = Blueprint(
    'pages',
    __name__,
    template_folder='templates')

TMPL = "<li><a href='/pages/{0}'>{0}</a></li>"

@blueprint.route('/pages')
def pages():
    query = db.session.query(Page.name.distinct().label("name"))
    names = [TMPL.format(row.name) for row in query.all()]
    return "".join(names), 200

@blueprint.route('/pages/<string:name>')
def page_by_name(name=None):
    if name:
        page = Page.query \
                   .filter_by(name=name) \
                   .order_by(Page.created_ts.desc()) \
                   .limit(1).first()
        if page:
            return page.html, 200
    return "<p>No page here</p>", 404
