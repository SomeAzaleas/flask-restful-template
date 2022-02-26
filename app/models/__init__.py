from .base import db


def init_app(app):
    db.init_app(app)
    # Import the models that need to create tables
    from .admin import Admin
