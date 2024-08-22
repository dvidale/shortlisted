from .db import db, environment, SCHEMA
from .user_job_title import user_job_titles

class Job_Title(db.Model):
    __tablename__ = 'job_titles'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(50), nullable=False)

    users = db.relationship('User', secondary = user_job_titles, back_populates='job_titles')