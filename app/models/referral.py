from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class Referral(db.Model):
    __tablename__ = 'referrals'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    shortlist_id= db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('shortlists.id')))
    referred_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')) )
    date_referred = db.Column(db.DateTime, nullable=False, default=db.func.now())

    comments = db.relationship('Comment', cascade='all, delete-orphan')