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


#  *GET MY REFERRAL THREADS

@shortlists_routes.route('/my-referrals/<int:id>')
def get_my_referrals(id):
    """
    - get shortlist title, description, search details, 
        creator first and last name, creator photo, and
        specific thread for the referred user for every shortlist where the current user is a referred user

        SELECT Shortlist.title, Shortlist.description, etc
        FROM Shortlists
        JOIN Referrals ON Shortlist.id == referral.shortlist_id

        SELECT User.first_name, User.last_name, User.profile_img
        FROM Users
        WHERE Shortlist.createdby_id == user.id

        SELECT Comments
        FROM Comments
        WHERE Comments.referral_id == referral_id

        WHERE referred_id == current_user_id

        referral {
        shortlist_info: "",
        creator_info: "",
        comments: []
        }
    """
    
    current_user = User.query.get(id)
    
    """
    get shortlist title, description, search details, 
        creator first and last name, creator photo, and
        ALSO
        get a comments thread array for every referral where the current user is a referred user
        
    """
    # TODO - This could be a single eager loaded query, but I took too long realizing I need to use SQLAlchemy v1.4 syntax instead of v2.0 to do it now
    # TODO - Also consider rewriting as a method on a model
    # TODO - I would much rather the comment threads be organized in an object for more performant updating
    try:
        stmt = db.select(Shortlist.id, Shortlist.title, User.first_name, User.last_name, User.profile_img_url).join(Shortlist.referrals).join(Shortlist.users).where(Referral.referred_id == current_user.id).order_by(Referral.id)
        
        results = db.session.execute(stmt)

        user_referrals = db.session.scalars(
            db.select(Referral).where(Referral.referred_id == current_user.id)
        ).all()

        ref_lst = []
        i=0
        for row in results:
            
            ref_obj = {
                'shortlist_id': row.id,
                'shortlist_title': row.title,
                'createdby_fname': row.first_name,
                'createdby_lname': row.last_name,
                'createdby_photo': row.profile_img_url,
                'comment_thread': [comment.to_dict() for comment in user_referrals[i].comments]
            }
            if len(ref_obj['comment_thread']) > 0:
                ref_lst.append(ref_obj)
            i+=1
    
        res_obj = {
            'referral_threads': ref_lst
        }

        if len(res_obj['referral_threads']) > 0:
            return res_obj, 200
        else:
            return {'error': 'No messages'}, 404
    except:
        return {'error': 'There was an error getting the referral messages'}, 500

    

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
    