from flask import Blueprint, request
from app.models import Shortlist, db, Job_Title, Genre, Industry_Area, Location
from app.forms.save_shortlist_form import SaveShortlistForm
import json

shortlists_routes = Blueprint('shortlists', __name__)

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
            created_by_id=created_by
        )

        print(">>> newShortlist", newShortlist.to_dict()) 

        return {'message': 'shortlist saved successfully'}
    
    return {'error': save_shortlist_form.errors}

# after the shortlist is created, created a referral record for each user in the shortlist

# shortlist_id
# referred_id
# date_referred