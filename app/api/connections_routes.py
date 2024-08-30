from flask import Blueprint, request
from app.models import User, db
from app.forms.search_connections_form import SearchConnectionsForm
import json
from dateutil import parser

connections_routes = Blueprint('connections', __name__)


# * BUILD A SHORTLIST
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
        # user_network are all the users the current user is connected to, rather by invitation sent or received

        request_data = request.json
        # .json turns request data into a dict
        # start_date = request_data['start_date']
        # end_date = request_data['end_date']

        # startDate = parser.parse(start_date)

        # if end_date != None:
        #     endDate = parser.parse(end_date)

        # if a parameter is present add its filter to filter list, if not, add its anti-filter
        location_matched = filter( lambda user: location[0] in user['locations'], user_network)

        industry_matched = filter(lambda user: industry_area[0] in user['industry_areas'], location_matched)

        job_title_matched = filter(lambda user: job_title[0] in user['job_title'], industry_matched)

        if(genre[0] != 'None'):

            genre_matched = filter(lambda user: genre[0] in user['genres'], job_title_matched)
        else:
            genre_matched = job_title_matched

# ? Moved availability check to frontend for easier date object comparisons, but saving the logic for reference
        # def availCheck(user):
        #     if len(user['bookings']) == 0:
        #         return True
        #     else:
                
        #         for booking in user['bookings']:
        #             bookingStart, bookingEnd = booking
        #             print(">>>> user's current booking", bookingStart, ", ", bookingEnd)
        #             print(">>>> job start date:", startDate)
        #             if bookingStart < startDate < bookingEnd: #checks if start date falls in the middle of current booking
        #                     return False
        #             if end_date != None:
        #                 if bookingStart < endDate < bookingEnd: #checks if the job ending overlaps with current booking dates
        #                     return False
        #                 if bookingStart < startDate and endDate < bookingEnd: #checks for current booking wrapping around job opp
        #                     return False
        #                 if startDate < bookingStart and bookingEnd < endDate: #checks if job opp wraps around current booking
        #                     return False
        #                 if startDate < bookingStart < endDate: #checks if current booking starts conflicts with job dates
        #                     return False
        #                 if startDate < bookingEnd < endDate: #checks if current booking ending conflicts with job dates
        #                     return False 
        #             else:
        #                 return True
    
        
        # avail_matched = filter(lambda user: availCheck(user), genre_matched)

        



        search_results = list(genre_matched)
        # print(">>>>>> search results", search_results)
        return search_results




    print(">>>>>0form errors:", searchForm.errors)
    return searchForm.errors, 400
    