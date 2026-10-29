"""Application factory for the Account microservice."""
import os

import click
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_talisman import Talisman

db = SQLAlchemy()


def create_app(test_config=None):
    """Create and configure the Flask application."""
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.getenv("SECRET_KEY", "local-development-only"),
        SQLALCHEMY_DATABASE_URI=os.getenv(
            "DATABASE_URL", "sqlite:///accounts.db"
        ),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
    if test_config:
        app.config.update(test_config)

    # HTTPS redirect is disabled for local development; production should terminate TLS.
    Talisman(
        app,
        force_https=not app.config.get("TESTING", False),
        content_security_policy={
            "default-src": ["'self'"],
            "object-src": ["'none'"],
            "frame-ancestors": ["'none'"],
        },
        referrer_policy="no-referrer",
        x_content_type_options=True,
        frame_options="DENY",
    )

    @app.after_request
    def apply_cors_headers(response):
        """Permit browser clients from local development origins."""
        origin = request_origin = os.getenv("CORS_ALLOWED_ORIGIN", "http://localhost:3000")
        incoming = app.request_class  # keep route setup independent of request globals
        from flask import request
        if request.headers.get("Origin") in (origin, "http://127.0.0.1:3000"):
            response.headers["Access-Control-Allow-Origin"] = request.headers["Origin"]
            response.headers["Vary"] = "Origin"
            response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
            response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        return response

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
