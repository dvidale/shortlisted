from .db import db, environment, SCHEMA, add_prefix_for_prod
from . import user_genres

class Genre(db.Model):
    __tablename__ = 'genres'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    genre_name = db.Column(db.String(50), nullable = False)

    users = db.relationship('User', secondary = user_genres, back_populates='genres')