from .db import db, environment, SCHEMA, add_prefix_for_prod
from .user_location import user_locations

class Location(db.Model):
    __tablename__ = 'locations'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(50), nullable = False)
    state = db.Column(db.String(50), nullable = True)
    country = db.Column(db.String(50), nullable = True)

    users = db.relationship('User', secondary = user_locations, back_populates='locations')