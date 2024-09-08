from flask import Blueprint, request
from app.models import db, Booking

from dateutil import parser

from app.models.user import User

bookings_routes = Blueprint('bookings', __name__)


#GET CURRENT USER'S BOOKINGS
@bookings_routes.route('/my-bookings/<int:id>')
def get_my_bookings(id):
    user = db.session.query(User).get(id)
    if(not user):
       return {'error': 'User not found'}, 404 

    user_bookings = user.bookings

    print("user_bookings",user_bookings)
    return [booking.to_dict() for booking in user_bookings]
