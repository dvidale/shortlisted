from .db import db, environment, SCHEMA, add_prefix_for_prod

user_genres = db.Table('user_genres',
                       db.Column('user_id', db.Integer, db.ForeignKey(add_prefix_for_prod('users.id'))),
                       db.Column('genre_id', db.Integer, db.ForeignKey(add_prefix_for_prod('genres.id')))

                       )

if environment == "production":
    user_genres.schema = SCHEMA