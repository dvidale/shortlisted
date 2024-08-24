from flask import Blueprint, request
from app.models import Shortlist, db
from app.forms.save_shortlist_form import SaveShortlistForm

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

    if save_shortlist_form.validate_on_submit():
        newShortlist = Shortlist()

        

# after the shortlist is created, created a referral record for each user in the shortlist

# shortlist_id
# referred_id
# date_referred