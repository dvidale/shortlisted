from flask import Blueprint, request
from app.models import User, db
from app.forms.search_connections_form import SearchConnectionsForm

connections_routes = Blueprint('connections', __name__)

@connections_routes.route('/<int:id>', methods=['POST'])
def search_connections(id):

    # user = User.query.get(id)
    # user_network = user.my_connections()

    # parameters
    # location = request.args.get('location')
    
    searchForm = SearchConnectionsForm()
    searchForm["csrf_token"].data = request.cookies["csrf_token"]
    
    location = searchForm.data['location']
    print(">>>>location from form in POST route:", location) 

    industry_areas = request.args.get('industry_areas')
    job_titles = request.args.get('job_titles')
    genres = request.args.get('genres')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')




    return {"message": "post route reached"}
    