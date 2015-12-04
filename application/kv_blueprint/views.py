from flask import (
    Blueprint,
    jsonify,
)
from ..extensions import auth, db
from ..models.kv import KV


blueprint = Blueprint(
    'kv',
    __name__,
    template_folder='templates',
    url_prefix='/latest/kv')


@blueprint.route('/')
def keys():
    query = db.session.query(KV.key.distinct().label("key"))
    keys = [{'key': row.key} for row in query.all()]
    return jsonify({'keys': keys}), 200

@blueprint.route('/<string:name>')
def by_key(name=None):
    if name:
        obj = KV.query \
                   .filter_by(key=name) \
                   .order_by(KV.created_ts.desc()) \
                   .limit(1).first()
        if obj:
            return jsonify(obj.value), 200
    return jsonify({'msg': 'Not found', 'status_code': 404}), 404
