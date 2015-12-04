from flask import (
    Blueprint,
)
from ..extensions import auth, db
from ..models.page import Page


ROOT = '/latest/page'

blueprint = Blueprint(
    'pages',
    __name__,
    template_folder='templates',
    url_prefix=ROOT)

TMPL = "<li><a href='{0}/{1}'>{1}</a></li>"

@blueprint.route('/')
def pages():
    query = db.session.query(Page.name.distinct().label("name"))
    names = [TMPL.format(ROOT, row.name) for row in query.all()]
    return "".join(names), 200

@blueprint.route('/<string:name>')
def page_by_name(name=None):
    if name:
        page = Page.query \
                   .filter_by(name=name) \
                   .order_by(Page.created_ts.desc()) \
                   .limit(1).first()
        if page:
            return page.html, 200
    return "<p>No page here</p>", 404
