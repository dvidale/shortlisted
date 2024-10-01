from flask import Blueprint, request
import json
from app.models import db, Booking
from app.forms.booking_form import BookingForm
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

    
    return [booking.to_dict() for booking in user_bookings]

#CREATE A NEW BOOKING
@bookings_routes.route('/new', methods=['POST'])
def create_booking():
    create_booking_form = BookingForm()
    create_booking_form["csrf_token"].data = request.cookies["csrf_token"]

    

    request_data = request.json
      # .json turns request data into a dict
    
    start_date = request_data['start_date']
    end_date = request_data['end_date']
   

    if create_booking_form.validate_on_submit():
        try:
            user_id = create_booking_form.data['user_id']
            shortlist_id = create_booking_form.data['shortlist_id']
             
            startDateParsed = parser.parse(start_date)
            endDateParsed = parser.parse(end_date)

            newBooking = Booking(
                user_id=user_id,
                shortlist_id= shortlist_id or None,
                start_date= None,
                end_date=endDateParsed
                )
            db.session.add(newBooking)
            db.session.commit()

            return newBooking.to_dict(), 200
        except:
            return {'error':{'error':'There was an error saving the booking'}}, 500
    # TODO: refactor these errors to not need this object nesting
    print ('booking_error', create_booking_form.errors)
    return {'error': create_booking_form.errors}, 400