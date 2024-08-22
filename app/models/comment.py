from .db import db, environment, SCHEMA, add_prefix_for_prod
import datetime

class Comment(db.Model):
    __tablename__ = 'comments'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}
    
    id = db.Column(db.Integer, primary_key=True)
    shortlist_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('shortlists.id')), nullable=False)
    commenter_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    text = db.Column(db.String(255), nullable = False)
    createdAt = db.Column(db.TIMESTAMP(timezone=True), nullable=False, default=db.func.now())
    updatedAt = db.Column(db.TIMESTAMP(timezone=True), nullable=False, default=db.func.now(), onupdate=db.func.now())