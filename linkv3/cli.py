import fire
import flask_migrate
from app import create_app
from flask import render_template
import settings


def run_server():
    app = create_app()
    @app.route('/')
    def index():
        return render_template('home.html')

    return app.run(host='0.0.0.0',port='8000',debug = True)

def migrate_init():

    app=create_app()
    with app.app_context():
        return flask_migrate.init('migrates')

def migrate(msg):

    app = create_app()
    with app.app_context():
        return flask_migrate.migrate('migrates',message = msg)

def revision(msg):

    app=create_app()
    with app.app_context():
        return flask_migrate.revision('migrates',message = msg)

def upgrade(revision='head'):

    app = create_app()
    with app.app_context():
        return flask_migrate.upgrade('migrates', revision)

def downgrade(revision='-1'):

    app = create_app()
    with app.app_context():
        return flask_migrate.downgrade('migrates', revision)

if __name__ =='__main__':
    fire.Fire({
        'run_server': run_server,
        'migrate_init': migrate_init,
        'migrate': migrate,
        'revision': revision,
        'upgrade': upgrade,
        'downgrade': downgrade

    })
