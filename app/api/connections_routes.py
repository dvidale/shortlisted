from flask import Blueprint, request
from app.models import User, db
from app.forms.search_connections_form import SearchConnectionsForm

connections_routes = Blueprint('connections', __name__)

@connections_routes.route('/<int:id>', methods=['POST'])
def search_connections(id):

    searchForm = SearchConnectionsForm()
    searchForm["csrf_token"].data = request.cookies["csrf_token"]
    
    location = searchForm.data['location']
    print('>>>>>>>location:', location)
    industry_area = searchForm.data['industry_area']
    job_title = searchForm.data['job_title']
    genre = searchForm.data['genre']
    # start_date = searchForm.data['start_date']
    # end_date = searchForm.data['end_date']

    if searchForm.validate_on_submit():
        user = User.query.get(id)
        user_network = user.my_connections()
        print(">>>>>user_Network", user_network)

        # if a parameter is present add its filter to filter list, if not, add its anti-filter
        location_matched = filter( lambda user: location[0] in user['locations'], user_network)

        industry_matched = filter(lambda user: industry_area[0] in user['industry_areas'], location_matched)

        job_title_matched = filter(lambda user: job_title[0] in user['job_title'], industry_matched)

        print(">>>>>genre:", genre[0])

        if(genre[0] != 'None'):

            genre_matched = filter(lambda user: genre[0] in user['genres'], industry_matched)

            return list(genre_matched)

        # unpack the filter list into a .filter_by method

        search_results = list(job_title_matched)
        print(">>>>>> search results", search_results)
        return search_results




    print(">>>>>>form errors:", searchForm.errors)
    return {"message": "form data rejected"}
    