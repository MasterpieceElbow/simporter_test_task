from flask import Flask

from .extensions import db
from .routes import api


def create_app(database_uri="sqlite:///./project.db"):
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "FesC9cBSuxakv9yN0vBY"
    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
    
    db.init_app(app)

    app.register_blueprint(api, url_prefix="/api")

    return app