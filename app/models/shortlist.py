from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime
from app.models.industry_area import Industry_Area
from app.models.job_title import Job_Title
from app.models.genre import Genre
from app.models.location import Location
from app.models.referral import Referral
from app.models.user import User

class Shortlist(db.Model):
    __tablename__ = "shortlists"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=True, default=None)
    job_title_id = db.Column(
        db.Integer, db.ForeignKey(add_prefix_for_prod("job_titles.id"))
    )
    industry_area_id = db.Column(
        db.Integer, db.ForeignKey(add_prefix_for_prod("industry_areas.id"))
    )
    genre_id = db.Column(
        db.Integer,
        db.ForeignKey(add_prefix_for_prod("genres.id")),
        nullable=True,
        default=None,
    )
    location_id = db.Column(
        db.Integer, db.ForeignKey(add_prefix_for_prod("locations.id"))
    )
    start_date = db.Column(db.DateTime, nullable=True, default=None)
    end_date = db.Column(db.DateTime, nullable=True, default=None)
    optional_img = db.Column(db.String(255), default=None)
    created_by_id = db.Column(
        db.Integer, db.ForeignKey(add_prefix_for_prod("users.id"))
    )
    createdAt = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updatedAt = db.Column(
        db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now()
    )

    referrals = db.relationship("Referral", cascade="all, delete-orphan")

    # comments = db.relationship('Comment', cascade="all, delete-orphan" )

    shortlist_referrals = db.relationship('User', secondary=add_prefix_for_prod('referrals'), back_populates='shortlistings')

    

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "job_title_id": self.job_title_id,
            "industry_area_id": self.industry_area_id,
            "genre_id": self.genre_id,
            "location_id": self.location_id,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "optional_img": self.optional_img,
            "created_by_id": self.created_by_id,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt,
        }
    
    def referral_list(self):
        return db.session.scalars(
                db.select(Referral.referred_id, Referral.id).where(Referral.shortlist_id == self.id)
            ).all()

    def single_view(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "industry_area": db.session.scalars(
                db.select(Industry_Area.industry_area).where(
                    Industry_Area.id == self.industry_area_id
                )
            ).first(),
            "job_title": db.session.scalars(
                db.select(Job_Title.job_title).where(Job_Title.id == self.job_title_id)
            ).first(),
            "genre": None
            or db.session.scalars(
                db.select(Genre.genre_name).where(Genre.id == self.genre_id)
            ).first(),
            "start_date":self.start_date,
            "end_date": self.end_date,
            "location": db.session.scalars(
                db.select(Location.city).where(Location.id == self.location_id)
            ).first(),
            'referral_name':[(user.first_name, user.last_name) for user in self.shortlist_referrals],
            'referral_idxs':db.session.scalars(
                db.select(Referral.id).where(Referral.shortlist_id == self.id)
            ).all()
            
            
        }
