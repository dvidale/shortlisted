from flask import Blueprint, request
from app.models import Shortlist, db, Job_Title
from app.forms.save_shortlist_form import SaveShortlistForm

shortlists_routes = Blueprint('shortlists', __name__)

@shortlists_routes.route('/new', methods=['POST'])
def save_shortlists():

    request_data = request.json

    print('request_data in save route:', request_data)


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
        
        job_title_id = db.select(Job_Title.id).where(Job_Title.job_title == '')

        
        newShortlist = Shortlist()

        return {'message': 'end of save shortlist route'}

# after the shortlist is created, created a referral record for each user in the shortlist

# shortlist_id
# referred_id
# date_referred