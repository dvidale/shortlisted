from flask import Blueprint, request
from app.models import Shortlist, db, Job_Title, Referral, Genre, Industry_Area, Location
from app.forms.save_shortlist_form import SaveShortlistForm
import json
from dateutil import parser
from datetime import datetime

shortlists_routes = Blueprint('shortlists', __name__)

# * SAVE A SHORTLIST
@shortlists_routes.route('/new', methods=['POST'])
def save_shortlists():

# write a route to collect the 
# shortlist name
# shortlist parameters
# description (optional)
# job_title_id
# industry_area_id
# genre_id (optional)
# location_id
# start_date
# end_date (optional)
# optional_img
# created_by(user_id)

    save_shortlist_form = SaveShortlistForm()
    save_shortlist_form["csrf_token"].data = request.cookies["csrf_token"]

    title = save_shortlist_form.data['title']
    description = save_shortlist_form.data['description']

    if save_shortlist_form.validate_on_submit():
        
        request_data = request.json
        # .json turns request data into a dict

        job_title = request_data['job_title']
        industry_area = request_data['industry_area']
        genre = request_data['genre']
        location = request_data['location']
        start_date = request_data['start_date']
        startDateParsed = parser.parse(start_date)
        # print(">>> start date parsed:", startDateParsed)
        end_date = request_data['end_date']
        endDateParsed = parser.parse(end_date)
        created_by = request_data['created_by']

        job_title_id = db.session.scalars(db.select(Job_Title.id).where(Job_Title.job_title == job_title)).first()

        industry_area_id = db.session.scalars(
            db.select(Industry_Area.id).where(Industry_Area.industry_area == industry_area)
        ).first()
        
        genreId = db.session.scalars(db.select(Genre.id).where(Genre.genre_name == genre)).first()

        locationId = db.session.scalars( db.select(Location.id).where(Location.city == location)).first()


        print(">>> data after queries", title, description, job_title_id, industry_area_id, genreId, locationId,created_by)
        
        newShortlist = Shortlist(
            title= title,
            description=description,
            job_title_id=job_title_id,
            industry_area_id=industry_area_id,
            genre_id=genreId,
            location_id=locationId,
            start_date=startDateParsed,
            end_date=endDateParsed,
            created_by_id=created_by
        )

        print(">>> newShortlist", newShortlist.to_dict()) 

        db.session.add(newShortlist)
        db.session.commit()

        return {'message': 'shortlist saved successfully'}
    
    return {'error': save_shortlist_form.errors}

# after the shortlist is created, created a referral record for each user in the shortlist

# shortlist_id
# referred_id
# date_referred


@shortlists_routes.route('/my-shortlists/<int:id>')
def getShortlists(id):
    shortlist_query = db.session.scalars(
        db.select(Shortlist).where(Shortlist.created_by_id == id)
    ).all()

    # for shortlist in shortlist_query:
    """
    SELECT Referral.id, User.first_name, User.last_name 
    FROM shortlists
    JOIN referrals
    WHERE (shortlist.id == referral.shortlist_id)
    JOIN Users
    WHERE (referral.referred_id == User.id)

     """
    
    referrals_query = db.session.scalars(
        db.select(Referral).where(Referral.shortlist_id == id)
    ).all()

    print(">>>>00 referral query:", referrals_query)

    referral_details = [ referral.with_details() for referral in  referrals_query ]

    print(">>>00 referral details", referral_details)

    print(">>>10 shortlist referral check:",[shortlist.single_view() for shortlist in shortlist_query] )
    return [shortlist.single_view() for shortlist in shortlist_query]