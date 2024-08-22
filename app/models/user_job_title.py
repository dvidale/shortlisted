from .db import db, environment, SCHEMA, add_prefix_for_prod



user_job_titles = db.Table(add_prefix_for_prod('user_job_titles'),
                           db.Column('user_id', db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), primary_key=True),
                           db.Column('job_title_id', db.Integer, db.ForeignKey(add_prefix_for_prod('job_titles.id')), primary_key=True),
                        
                            **({'schema': SCHEMA} if environment == "production" else {})
                           )
