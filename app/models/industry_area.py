from .db import db, environment, SCHEMA
from .user_industry import user_industries

class Industry_Area(db.Model):
    __tablename__ = 'industry_areas'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    industry_area = db.Column(db.String(100), nullable = False)

    users = db.relationship('User', secondary = user_industries, back_populates='industry_areas')

  