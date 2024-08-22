from .db import db, environment, SCHEMA, add_prefix_for_prod

user_industries = db.Table(add_prefix_for_prod('user_industries'),
                           db.Column('user_id', db.Integer, db.ForeignKey(add_prefix_for_prod('user.id'))),

                            **({'schema': SCHEMA} if environment == "production" else {})

)