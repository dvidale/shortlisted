from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class Referral(db.Model):
    __tablename__ = 'referrals'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    shortlist_id= db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('shortlists.id')))
    referrer_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')) )
    reffered_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')) )
    date_referred = db.Column(db.TIMESTAMP(timezone=True), nullable=False, default=db.func.now())