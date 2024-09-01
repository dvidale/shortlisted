from .db import db, environment, SCHEMA, add_prefix_for_prod
import datetime
from app.models.user import User

class Comment(db.Model):
    __tablename__ = 'comments'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    
    id = db.Column(db.Integer, primary_key=True,unique=True, autoincrement=True)
    shortlist_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('shortlists.id'), ondelete='CASCADE'), nullable=False)
    commenter_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    referral_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('referrals.id'), ondelete='CASCADE'), nullable=False)
    text = db.Column(db.String(255), nullable = False)
    createdAt = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updatedAt = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())


    referrals = db.relationship('Referral', back_populates = 'comments')
    shortlists = db.relationship('Shortlist', back_populates = 'comments')

    def to_dict(self):
        return{
            'id': self.id,
            'shortlist_id': self.shortlist_id,
            'commenter_id': self.commenter_id,
            'referral_id': self.referral_id,
            'commenter_name':db.session.scalars(
                db.select(User.first_name).where(User.id == self.commenter_id)
            ).first(),
            'text': self.text,
            'createdAt': self.createdAt,
            'updatedAt': self.updatedAt

        }
    
    