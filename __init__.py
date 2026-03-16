from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///microloan.db'
    app.config['SECRET_KEY'] = 'secret-key'

    db.init_app(app)

    from app.routes import auth_routes, user_routes, dev_routes
    app.register_blueprint(auth_routes.bp)
    app.register_blueprint(user_routes.bp)
    app.register_blueprint(dev_routes.bp)

    return app
