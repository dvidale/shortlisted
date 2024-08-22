from .db import db, environment, SCHEMA, add_prefix_for_prod
from datetime import datetime

class Connection(db.Model):
    __tablename__ = 'connections'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')) )
    connected_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')) )
    connection_type = db.Column(db.String(50), nullable=False)
    connection_context = db.Column(db.String(100), nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.now(datetime.UTC))
    updatedAt = db.Column(db.DateTime, nullable=False, default=datetime.now(datetime.UTC), onupdate=datetime.now(datetime.UTC))