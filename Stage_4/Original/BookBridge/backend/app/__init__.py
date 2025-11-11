import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_cors import CORS
from .config import Config

db = SQLAlchemy()
jwt = JWTManager()
migrate = Migrate()

def create_app(config_object=None):
    app = Flask(__name__, static_folder=None)
    app.config.from_object(config_object or Config)

    CORS(app)
    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    # register blueprints
    from .routes.auth import auth_bp
    from .routes.books import books_bp
    from .routes.reviews import reviews_bp

    app.register_blueprint(auth_bp, url_prefix="/api/v1/auth")
    app.register_blueprint(books_bp, url_prefix="/api/v1/books")
    app.register_blueprint(reviews_bp, url_prefix="/api/v1/reviews")

    # create db for sqlite during first run
    with app.app_context():
        db.create_all()

    return app

