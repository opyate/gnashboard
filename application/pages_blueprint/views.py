from flask import (
    Blueprint,
    request,
    jsonify,
    Response,
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

@blueprint.route('/<string:name>', methods=['GET'])
def get_page_by_name(name=None):
    if name:
        page = Page.query \
                   .filter_by(name=name) \
                   .order_by(Page.created_ts.desc()) \
                   .limit(1).first()
        if page:
            # TODO fix the newline issue
            _html = page.html
            html = _html.replace('\\012','\n')
            return html, 200
    return "<p>No page here</p>", 404

@blueprint.route('/<string:name>', methods=['POST'])
def post_page_by_name(name=None):
    if name:
        html = request.files['html']
        if html:
            page = Page(name=name, html=html.read())
            db.session.add(page)
            db.session.commit()
            return 'Created', 201
    return "<p>No page here</p>", 404
