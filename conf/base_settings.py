import os

_here = os.path.abspath(os.path.dirname(__file__))
_db_path = os.path.join(_here, '../store.sqlite')

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(_db_path)
