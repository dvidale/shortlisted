from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import datetime
from .user_job_title import user_job_titles
from .user_industry import user_industries
from .user_genre import user_genres
from .user_location import user_locations





class User(db.Model, UserMixin):
    __tablename__ = 'users'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable = False)
    last_name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    phone_number = db.Column(db.String(20))
    username = db.Column(db.String(40), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    profile_img_url = db.Column(db.String(255))
    receivedMsgs = db.Column(db.Integer, server_default='0')
    createdAt = db.Column(db.DateTime, nullable=False, default=db.func.now())
    updatedAt = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now())

    job_titles = db.relationship('Job_Title', secondary = user_job_titles, back_populates='users')

    industry_areas = db.relationship('Industry_Area', secondary= user_industries, back_populates='users')

    genres = db.relationship('Genre', secondary = user_genres, back_populates='users')

    locations = db.relationship('Location', secondary = user_locations, back_populates='users')

    connections_initiated = db.relationship('Connection', foreign_keys='Connection.user_id', back_populates='initiator', cascade='all, delete-orphan')

    connections_received = db.relationship('Connection', foreign_keys='Connection.connected_id', back_populates='receiver', cascade='all, delete-orphan')

    shortlists = db.relationship('Shortlist', cascade='all, delete-orphan', backref = 'users')

    shortlistings = db.relationship('Shortlist',
    secondary=add_prefix_for_prod('referrals'), back_populates='shortlist_referrals' )

    bookings = db.relationship('Booking', backref='users', cascade='all, delete-orphan')

    referrals = db.relationship('Referral', cascade='all, delete-orphan')




    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def my_connections(self):
        # return the user records for all the users who have any connection with the current user
        
        initiated = [User.query.get(connection.connected_id) for connection in self.connections_initiated]

        received = [User.query.get(connection.user_id) for connection in self.connections_received]

        connections_lst = [user.to_dict() for user in initiated + received]

        return connections_lst


    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone_number': self.phone_number,
            'job_title': [ title.job_title for title in self.job_titles],
            'industry_areas': [name.industry_area for name in self.industry_areas ],
            'genres':[ name.genre_name for name in self.genres ],
            'locations': [name.city for name in self.locations],
            'bookings': [(booking.start_date, booking.end_date) for booking in self.bookings],
            'profile_img_url': self.profile_img_url
        }
    
    def search_result(self):
        return{
            'id':self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'profile_img_url': self.profile_img_url
        }
