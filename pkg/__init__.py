from flask import Flask
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

migrate = Migrate()
csrf = CSRFProtect()


def create_app():
    from pkg.models import db
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    csrf.init_app(app)
    migrate.init_app(app,db)
    return app

app = create_app()

from pkg import admin_routes, user_routes