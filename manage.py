import click
from flask import Flask
from flask_migrate import Migrate, init, migrate, upgrade

from settings import settings


def create_app(setting='default'):
    from app import models, routes
    app = Flask(__name__)
    app.config.from_object(settings[setting])
    models.init_app(app)
    routes.init_app(app)
    return app


def run_dev():
    app = create_app(setting='dev')
    app.run()


def run_prod():
    app = create_app(setting='dev')
    app.run()


def db_init_dev():
    app = create_app(setting='dev')
    from app.models.base import db
    with app.app_context():
        Migrate(app, db)
        init()
        migrate(message="Initial migration")
        upgrade()


def db_init_prod():
    app = create_app(setting='prod')
    from app.models.base import db
    with app.app_context():
        Migrate(app, db)
        init(directory='prod_migrations')
        migrate(directory='prod_migrations', message="Initial migration")
        upgrade(directory='prod_migrations')


def db_migrate_dev():
    app = create_app(setting='dev')
    from app.models.base import db
    with app.app_context():
        Migrate(app, db)
        migrate()
        upgrade()


def db_migrate_prod():
    app = create_app(setting='prod')
    from app.models.base import db
    with app.app_context():
        Migrate(app, db)
        migrate(directory='prod_migrations')
        upgrade(directory='prod_migrations')


env_settings = {
    'dev': run_dev,
    'prod': run_prod
}

db_init_settings = {
    'dev': db_init_dev,
    'prod': db_init_prod
}

db_migrate_settings = {
    'dev': db_migrate_dev,
    'prod': db_migrate_prod
}


@click.group()
def cmds():
    pass


@cmds.command('runserver')
@click.option('--env', '-e', type=click.Choice(list(env_settings.keys())), required=True)
def runserver(env):
    env_settings[env]()


@cmds.command('db')
@click.option('--operate', '-o', type=click.Choice(['init', 'migrate']), required=True)
@click.option('--env', '-e', type=click.Choice(list(env_settings.keys())), required=True)
def db(operate, env):
    operates = {
        'init': db_init_settings,
        'migrate': db_migrate_settings
    }
    operates[operate][env]()


if __name__ == '__main__':
    cmds()
