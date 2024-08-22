from .db import db, environment, SCHEMA, add_prefix_for_prod

user_industries = db.Table(add_prefix_for_prod('user_industries'),
                           db.Column('user_id', db.Integer, db.ForeignKey(add_prefix_for_prod('users.id'))),
                           db.Column('industry_area_id', db.Integer, db.ForeignKey(add_prefix_for_prod('industry_areas.id'))),

                            **({'schema': SCHEMA} if environment == "production" else {})

)