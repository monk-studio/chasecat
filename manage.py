import click
from flask.cli import FlaskGroup
from flask_alembic import Alembic


def _create_flask_app(_):
    from leaderboard import create_app
    app = create_app()
    Alembic(app)
    return app


@click.group(cls=FlaskGroup, create_app=_create_flask_app)
def cli():
    pass


if __name__ == '__main__':
    cli()
