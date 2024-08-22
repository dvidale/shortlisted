from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime


class Shortlist(db.Model):
    __tablename__ = 'shortlists'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    job_title_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('job_titles.id')) )
    industry_area_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('industry_areas.id')) )
    genre_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('genres.id')) )
    location_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('locations.id')))
    start_date = db.Column(db.DateTime, nullable = True)
    end_date = db.Column(db.DateTime, nullable = True)
    optional_img = db.Column(db.String(255))
    created_by_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')) )
    createdAt = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updatedAt = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())
    