from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pets Table for db"""

    __tablename__ = 'pets'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text, 
                    nullable=False)
    species = db.Column(db.Text, 
                    nullable=False)
    photo_url = db.Column(db.Text, 
                    nullable=True, 
                    default='https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/1024px-No_image_available.svg.png')
    age = db.Column(db.Integer, 
                    nullable=True)
    notes = db.Column(db.Text, 
                    nullable=True)
    available = db.Column(db.Boolean, 
                    nullable=False,
                    default=True)
