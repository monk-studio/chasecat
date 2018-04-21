from .base import db
from .record import Record


def init_app(app):
    db.init_app(app)
