from .db import db, environment, SCHEMA, add_prefix_for_prod

user_locations = db.Table(add_prefix_for_prod('user_locations'),
                          db.Column('user_id', db.Integer, db.ForeignKey(add_prefix_for_prod('users.id'))),
                          db.Column('location_id', db.Integer, db.ForeignKey(add_prefix_for_prod('locations.id'))),

                          **({'schema': SCHEMA} if environment == "production" else {})

                          )

