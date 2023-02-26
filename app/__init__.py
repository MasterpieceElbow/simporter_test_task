from flask import Flask

from .extensions import db
from .routes import api


def create_app(database_uri="sqlite:///./project.db"):
    app = Flask(__name__)

    if app.config["ENV"] == "production":
        app.config.from_object("config.ProductionConfig")
    else:
        app.config.from_object("config.DevelopmentConfig")
    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(api, url_prefix="/api")

    return app