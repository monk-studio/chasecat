from flask import Blueprint, redirect, render_template

from chasecat.models import Record

bp = Blueprint('front', __name__)


@bp.route('/')
def to_home():
    return redirect('https://monk-studio.com', 302)


@bp.route('invite/<uid>')
def invite(uid):
    record = Record.query.filter_by(user_id=uid).first()
    if not record:
        raise 404
    return render_template('invite.html', record=record)
