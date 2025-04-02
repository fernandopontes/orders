from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    database_url = os.getenv('DATABASE_URL')
    if not database_url:
        raise RuntimeError("A variável de ambiente 'DATABASE_URL' não está definida!")
    
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    with app.app_context():
        from . import models
        from .routes import routes
        app.register_blueprint(routes)
        db.create_all()

    return app