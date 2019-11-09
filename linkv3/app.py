import connexion
from flask import render_template
from models import db,migrate

from flask_migrate import Migrate
from settings import Set


def create_app():
    _app = connexion.FlaskApp(__name__,specification_dir = '.')
    _app.app.config.from_object(Set)
    _app.add_api('swagger.yml')
    db.init_app(_app.app)
    migrate.init_app(_app.app,db)


    return _app.app




