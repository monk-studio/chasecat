import base64

from Crypto.Cipher import AES
from flask import Blueprint, request, jsonify, current_app
from leaderboard.models import db, Record

bp = Blueprint('api', __name__)


@bp.route('/summary')
def summary():
    tops = Record.query.order_by(Record.score.desc()) \
        .limit(100).all()
    rv = dict(tops=tops)
    me = request.args.get('me')
    if me:
        me = Record.query.filter_by(user_id=me).first()
        if me:
            ahead = Record.query.filter(Record.score > me.score) \
                .count()
            rv['me'] = dict(**me.to_dict(), rank=ahead + 1)
    return jsonify(rv)


@bp.route('/submit', methods=['POST'])
def submit():
    payload = request.get_json()
    user_id = payload['user_id']
    user_name = payload['user_name']
    score = payload['score']

    c = AES.new(current_app.config['SHA256_KEY'], AES.MODE_CBC,
                current_app.config['SHA256_IV'])
    score = int(c.decrypt(base64.b64decode(score)))

    src = Record.query.filter_by(user_id=user_id).first()
    if not src:
        src = Record()
    src.user_name = user_name
    src.score = score
    src.user_id = user_id
    with db.auto_commit():
        db.session.add(src)
    return jsonify(src)
