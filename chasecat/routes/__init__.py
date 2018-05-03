from . import api, front


def init_app(app):
    @app.route('/static/<path:path>')
    def static_file(path):
        return app.send_static_file(path)

    app.register_blueprint(front.bp, url_prefix='/')
    app.register_blueprint(api.bp, url_prefix='/api')
