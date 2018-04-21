from flask import Blueprint, request, jsonify
from leaderboard.models import db, Leaderboard

bp = Blueprint('api', __name__)


@bp.route('/summary')
def summary():
    tops = Leaderboard.query.order_by(Leaderboard.score.desc()) \
        .limit(100).all()
    rv = dict(tops=tops)
    me = request.args.get('me')
    if me:
        me = Leaderboard.query.filter_by(user_id=me).first()
        if me:
            ahead = Leaderboard.query.filter(Leaderboard.score > me.score) \
                .count()
            rv['me'] = dict(**me.to_dict(), rank=ahead + 1)
    return jsonify(rv)


@bp.route('/submit', methods=['POST'])
def submit():
    payload = request.get_json()
    user_id = payload['user_id']
    user_name = payload['user_name']
    score = payload['score']

    src = Leaderboard.query.filter_by(user_id=user_id).first()
    if not src:
        src = Leaderboard()
    src.user_name = user_name
    src.score = score
    src.user_id = user_id
    with db.auto_commit():
        db.session.add(src)
    return jsonify(src)
