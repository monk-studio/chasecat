import base64

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from flask import Blueprint, request, jsonify, current_app
from leaderboard.models import db, Record

bp = Blueprint('api', __name__)


@bp.route('/summary')
def summary():
    tops = Record.query.order_by(Record.score.desc()) \
        .limit(50).all()
    rv = dict(tops=tops)
    me = request.args.get('me')
    if me:
        me = Record.query.filter_by(user_id=me).first()
        if me:
            ahead = Record.query.filter(Record.score > me.score) \
                .count()

            def sort(x):
                if x.score == me.score:
                    return x.score + 0.1 if x.id == me.id else x.score
                else:
                    return x.score

            rv['tops'] = sorted(tops, key=sort, reverse=True)
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
    raw = base64.b64decode(score)
    raw = unpad(c.decrypt(raw), 16).decode()
    score = int(raw)

    src = Record.query.filter_by(user_id=user_id).first()
    if not src:
        src = Record()
    src.user_name = user_name
    src.score = score
    src.user_id = user_id
    with db.auto_commit():
        db.session.add(src)
    return jsonify(src)
