from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True  # do not create table for Base
    create_time = db.Column(db.DateTime, server_default=db.func.now())
    update_time = db.Column(db.DateTime, onupdate=db.func.now())
    delete_time = db.Column(db.DateTime)
