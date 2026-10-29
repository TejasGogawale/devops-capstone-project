"""Application factory for the Account microservice."""
import os

import click
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(test_config=None):
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI=os.getenv(
            "DATABASE_URL", "sqlite:///accounts.db"
        ),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
    if test_config:
        app.config.update(test_config)

    db.init_app(app)

    from service.routes import accounts_blueprint
    app.register_blueprint(accounts_blueprint)

    @app.cli.command("db-create")
    def db_create():
        """Create all database tables."""
        with app.app_context():
            from service.models import Account  # noqa: F401
            db.create_all()
        click.echo("Account database tables created.")

    return app
