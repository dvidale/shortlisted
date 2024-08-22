from .db import db, environment, SCHEMA, add_prefix_for_prod

user_genres = db.Table(add_prefix_for_prod('user_genres'),
                       db.Column('user_id', db.Integer, db.ForeignKey(add_prefix_for_prod('users.id'))),
                       db.Column('genre_id', db.Integer, db.ForeignKey(add_prefix_for_prod('genres.id'))),

                        **({'schema': SCHEMA} if environment == "production" else {})


                       )