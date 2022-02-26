# here is an example to create model
# you should always import db from .base to create a new model
from .base import db, Base


class Admin(Base):
    __tablename__ = 'admin'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    __maper_args__ = {
        'concrete': True
    }
