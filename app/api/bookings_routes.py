from flask import Blueprint, request
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

    print("user_bookings",user_bookings)
    return [booking.to_dict() for booking in user_bookings]

#CREATE A NEW BOOKING
@bookings_routes.route('/new', methods=['POST'])
def create_booking():
    create_booking_form = BookingForm()
    create_booking_form["csrf_token"].data = request.cookies["csrf_token"]

    if create_booking_form.validate_on_submit():
        
        user_id = create_booking_form.data['user_id']
        shortlist_id = create_booking_form.data['shortlist_id']
        start_date = create_booking_form.data['start_date']
        end_date = create_booking_form.data['end_date']
        
        startDateParsed = parser.parse(start_date)
        endDateParsed = parser.parse(end_date)

        newBooking = Booking(
            user_id=user_id,
            shortlist_id= shortlist_id or None,
            start_date=startDateParsed,
            end_date=endDateParsed
            )
        db.session.add(newBooking)
        db.session.commit()

        return newBooking.to_dict(), 200
    
    return {'error': create_booking_form.errors}, 400