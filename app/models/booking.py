from enum import unique
from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Booking(db.Model):
    __tablename__ = 'bookings'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')) )
    shortlist_id= db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('shortlists.id')))
    start_date = db.Column(db.DateTime, nullable = False)
    end_date = db.Column(db.DateTime, nullable = False)
    createdAt = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updatedAt = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())

    # users = db.relationship('User')

    def to_dict(self):
        return{
            'id': self.id,
            'user_id': self.user_id,
            'shortlist_id': self.shortlist_id,
            'start_date':self.start_date,
            'end_date':self.end_date,
            'createdAt':self.createdAt,
            'updatedAt': self.updatedAt,
            'activity_type': 'booking'
        }