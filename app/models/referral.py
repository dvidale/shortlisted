from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime
from app.models.user import User

class Referral(db.Model):
    __tablename__ = 'referrals'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    shortlist_id= db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('shortlists.id')))
    referred_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')) )
    date_referred = db.Column(db.DateTime, nullable=False, default=db.func.now())

    comments = db.relationship('Comment', cascade='all, delete-orphan')

    def with_details(self):
        return{
            'id': self.id,
            'shortlist_id':self.shortlist_id,
            'referred_first_name': db.session.scalars(
                db.select(User.first_name).where(Referral.referred_id == User.id)
            ).first(),
             'referred_last_name': db.session.scalars(
                db.select(User.last_name).where(Referral.referred_id == User.id)
            ).first(),
            'date_referred': self.date_referred
        }