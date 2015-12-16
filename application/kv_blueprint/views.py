from flask import (
    Blueprint,
    jsonify,
    request,
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

@blueprint.route('/<string:key>', methods=['GET'])
def get_kv_by_key(key=None):
    if key:
        obj = KV.query \
                   .filter_by(key=key) \
                   .order_by(KV.created_ts.desc()) \
                   .limit(1).first()
        if obj:
            return jsonify(obj.value), 200
    return jsonify({'msg': 'Not found', 'status_code': 404, 'key': key}), 404

@blueprint.route('/<string:key>', methods=['POST'])
def post_kv_by_key(key=None):
    if key:
        json = request.get_json(force=True)
        if json:
            kv = KV(key=key, value=json)
            db.session.add(kv)
            db.session.commit()
            return jsonify({'msg': 'Created', 'status_code': 201, 'key': key}), 201
    return jsonify({'msg': 'Not found', 'status_code': 404, 'key': key}), 404
