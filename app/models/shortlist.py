from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class Shortlist(db.Model):
    __tablename__ = 'shortlists'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True, default=None)
    job_title_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('job_titles.id')) )
    industry_area_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('industry_areas.id')) )
    genre_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('genres.id')), nullable=True, default=None)
    location_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('locations.id')))
    start_date = db.Column(db.DateTime, nullable = True, default=None)
    end_date = db.Column(db.DateTime, nullable = True, default=None)
    optional_img = db.Column(db.String(255), default=None)
    created_by_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')) )
    createdAt = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updatedAt = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())

    referrals = db.relationship('Referral', cascade='all, delete-orphan')

    def to_dict(self):
        return{
            'id':self.id,
            'title': self.title,
            'description': self.description,
            'job_title_id': self.job_title_id,
            'industry_area_id': self.industry_area_id,
            'genre_id': self.genre_id,
            'location_id':self.location_id,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'optional_img': self.optional_img,
            'created_by_id': self.created_by_id,
            'createdAt':self.createdAt,
            'updatedAt': self.updatedAt
        }
        
    