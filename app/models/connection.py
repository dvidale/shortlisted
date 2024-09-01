from .db import db, environment, SCHEMA, add_prefix_for_prod


class Connection(db.Model):
    __tablename__ = 'connections'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')) )
    connected_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')) )
    connection_type = db.Column(db.String(50), nullable=False)
    connection_context = db.Column(db.String(100), nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updatedAt = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())

    initiator = db.relationship('User', foreign_keys='Connection.user_id', back_populates='connections_initiated')

    receiver = db.relationship('User', foreign_keys='Connection.connected_id', back_populates='connections_received')

