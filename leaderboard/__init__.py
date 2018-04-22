import os
import datetime

from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder
from . import routes
from . import models


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'to_dict'):
            return o.to_dict()
        if isinstance(o, datetime.datetime):
            return o.strftime('%Y-%m-%dT%H:%M:%SZ')
        return _JSONEncoder.default(self, o)


class Flask(_Flask):
    json_encoder = JSONEncoder


def create_app():
    app = Flask(__name__)

    base_settings = os.path.join(app.root_path, '../conf/base_settings.py')
    app.config.from_pyfile(base_settings)

    local_settings = os.path.join(app.root_path, '../local_settings.py')
    app.config.from_pyfile(local_settings)

    routes.init_app(app)
    models.init_app(app)
    return app
