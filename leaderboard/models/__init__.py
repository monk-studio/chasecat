from .base import db
from .leaderboard import Leaderboard


def init_app(app):
    db.init_app(app)
