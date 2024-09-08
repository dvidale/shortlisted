from flask import Blueprint, request
from app.models import Shortlist, db, Job_Title, Referral, Genre, Industry_Area, Location
from app.forms.save_shortlist_form import SaveShortlistForm
import json
from dateutil import parser
from datetime import datetime

from app.models.comment import Comment
from app.models.user import User

shortlists_routes = Blueprint('shortlists', __name__)


# * SAVE A SHORTLIST
@shortlists_routes.route('/new', methods=['POST'])
def save_shortlists():

    save_shortlist_form = SaveShortlistForm()
    save_shortlist_form["csrf_token"].data = request.cookies["csrf_token"]

    title = save_shortlist_form.data['title']
    description = save_shortlist_form.data['description']
    request_data = request.json
      # .json turns request data into a dict

    created_by = request_data['created_by']

    # Unique title check
    title_found = db.session.scalars(
        db.select(Shortlist.title).filter(User.id == created_by).where(Shortlist.title == title)
    ).first()

    if(title_found):
        return {'error': 'Titles must be unique'}, 400


    if save_shortlist_form.validate_on_submit():
        
        job_title = request_data['job_title']
        industry_area = request_data['industry_area']
        genre = request_data['genre']
        location = request_data['location']
        start_date = request_data['start_date']
        startDateParsed = parser.parse(start_date)
        # print(">>> start date parsed:", startDateParsed)
        end_date = request_data['end_date']
        if(end_date != None):
           endDateParsed = parser.parse(end_date)
        else:
            endDateParsed = None
        created_by = created_by
        referrals = request_data['referrals']

        print(">>>>>> referrals entering save route", referrals)

        job_title_id = db.session.scalars(db.select(Job_Title.id).where(Job_Title.job_title == job_title)).first()

        industry_area_id = db.session.scalars(
            db.select(Industry_Area.id).where(Industry_Area.industry_area == industry_area)
        ).first()
        
        genreId = db.session.scalars(db.select(Genre.id).where(Genre.genre_name == genre)).first()

        locationId = db.session.scalars( db.select(Location.id).where(Location.city == location)).first()


        # print(">>> data after queries", title, description, job_title_id, industry_area_id, genreId, locationId,created_by)
        
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

        # print(">>> newShortlist", newShortlist.to_dict()) 

        db.session.add(newShortlist)
        db.session.commit()
# after the shortlist is created, created a referral record for each user in the shortlist

        currentShortlist = db.session.scalars(
            db.select(Shortlist).filter(Shortlist.created_by_id == created_by).where(Shortlist.title == title)
        ).first()

        # print(">>>>> currentShortlist record:", currentShortlist)

        for referral in referrals:
            newReferral = Referral(
                shortlist_id = currentShortlist.id,
                referred_id= referral['id']
            )
            db.session.add(newReferral)
            db.session.commit()

        return currentShortlist.single_view(), 201
    
    # print('> save shortlist error', save_shortlist_form.errors)
    return {'serverError': save_shortlist_form.errors}, 400


# * GET MY SHORTLISTS

@shortlists_routes.route('/my-shortlists/<int:id>')
def getShortlists(id):
    shortlist_query = db.session.scalars(
        db.select(Shortlist).where(Shortlist.created_by_id == id)
    ).all()


    return [shortlist.single_view() for shortlist in shortlist_query]

## * UPDATE A SHORTLIST

@shortlists_routes.route('<int:id>', methods = ['PUT'])
def updateShortlist(id):
    
    update_form = SaveShortlistForm()
    update_form["csrf_token"].data = request.cookies["csrf_token"]

    title = update_form.data['title']
    description = update_form.data['description']

    if update_form.validate_on_submit():
       shortlist = db.session.scalars(
           db.select(Shortlist).where(Shortlist.id == id)
       ).first() 


       shortlist.title = title
       shortlist.description = description

       db.session.commit()

       return shortlist.single_view(), 200

    return {'error': update_form.errors}, 400


# * DELETE A SHORTLIST
@shortlists_routes.route('/<int:id>', methods=['DELETE'])
def deleteShortlist(id):

    try:
        target_shortlist = db.session.scalars(
            db.select(Shortlist).where(Shortlist.id == id)
        ).first()

        # create a list of all the referral_ids to clear the state
        referrals_lst = db.session.scalars(
            db.select(Referral.id).where(Referral.shortlist_id == target_shortlist.id)
        ).all()

        # Manually deleting all associated comments before deleting shortlist
        db.session.query(Comment).filter(Comment.shortlist_id == target_shortlist.id).delete()
        db.session.commit()

        db.session.delete(target_shortlist)
        db.session.commit()

        success_msg = {'message': "Shortlist deleted successfully"}

        return [referrals_lst, success_msg]
    
    except:
        return {'error': 'There was an error deleting the shortlist'}, 500

# *DELETE A REFERRAL FROM A SHORTLIST
@shortlists_routes.route('/referrals/<int:id>', methods=['DELETE'])
def deleteReferral(id):

    try:
        target_referral = db.session.scalars(
            db.select(Referral).where(Referral.id == id)
            ).first()
        
        db.session.delete(target_referral)
        db.session.commit()
    except:
        return {'error': 'There was an error deleting the referral'}, 500

    return {"message": "Shortlist member deleted successfully"}
    