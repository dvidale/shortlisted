from flask import Blueprint, request
from app.models import User, db
from app.forms.search_connections_form import SearchConnectionsForm
import json
from dateutil import parser

connections_routes = Blueprint('connections', __name__)


# * SEARCH CONNECTIONS
@connections_routes.route('/<int:id>', methods=['POST'])
def search_connections(id):

    searchForm = SearchConnectionsForm()
    searchForm["csrf_token"].data = request.cookies["csrf_token"]
    
    location = searchForm.data['location']
    # print('>>>>>>>location:', location)
    industry_area = searchForm.data['industry_area']
    job_title = searchForm.data['job_title']
    genre = searchForm.data['genre']

    # * I'm using the react datepicker library input fields for the dates
    # start_date = searchForm.data['start_date']
    # end_date = searchForm.data['end_date']

    

    if searchForm.validate_on_submit():
        user = User.query.get(id)
        user_network = user.my_connections()
        # user_network are all the users the current user is connected to, whether by invitation sent or received

        request_data = request.json
        # .json turns request data into a dict
       
        # if a parameter is present add its filter to filter list, if not, add its anti-filter
        location_matched = filter( lambda user: location[0] in user['locations'], user_network)

        industry_matched = filter(lambda user: industry_area[0] in user['industry_areas'], location_matched)

        job_title_matched = filter(lambda user: job_title[0] in user['job_title'], industry_matched)
        # print(">>>>>> job_title_matched", list(job_title_matched))
       
        genre_matched = None

        if(genre[0] != 'None'):
            
            genre_matched = filter(lambda user: genre[0] in user['genres'], job_title_matched)
        else:
            
            genre_matched = filter(lambda user: genre[0] not in user['genres'], job_title_matched)



  
        # ? filter object returns an iterable but not a list, so it has to be wrapped before sending

        search_results_lst = list(genre_matched)
        # ? this list comp removes duplicates from the list
        search_results = [i for n, i in enumerate( search_results_lst) if i not in  search_results_lst[:n]]
        
        if len(search_results) == 0:
            return {'errors':'Sorry, none of your connections match this search.'}, 404
        
        return search_results, 200
        # ? Moved availability check to frontend for easier date object comparisons

    # print(">>>>>0form errors:", searchForm.errors)
    return searchForm.errors, 400
    