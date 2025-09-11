import re
from unittest import result
from flask import Blueprint, g, request
from app.forms import new_connection_form
from app.models import User, db, Connection
from app.models.db import add_prefix_for_prod
from app.forms.search_connections_form import SearchConnectionsForm
import json
from dateutil import parser
from app.forms.new_connection_form import NewConnectionsForm
from sqlalchemy import text

connections_routes = Blueprint("connections", __name__)


# * CACHE ALL CURRENT CONNECTIONS
@connections_routes.route("/cache/<int:id>", methods=["GET"])
def cache_connections(id):
    user = User.query.get(id)
    user_network = user.my_connections()

    return {"connections_cache": user_network}, 200


# * SEARCH CONNECTIONS
@connections_routes.route("/<int:id>", methods=["POST"])
def search_connections(id):

    searchForm = SearchConnectionsForm()
    searchForm["csrf_token"].data = request.cookies["csrf_token"]

    location = searchForm.data["location"]
    # print('>>>>>>>location:', location)
    industry_area = searchForm.data["industry_area"]
    job_title = searchForm.data["job_title"]
    genre = searchForm.data["genre"]

    # * I'm using the react datepicker library input fields for the dates
    # start_date = searchForm.data['start_date']
    # end_date = searchForm.data['end_date']

    if searchForm.validate_on_submit():

        if genre[0] == "None":
            sql = text(f"""SELECT users.id
                    FROM {add_prefix_for_prod('users')}
                    JOIN {add_prefix_for_prod('connections')} on connections.connected_id = users.id 
                    JOIN {add_prefix_for_prod('user_job_titles')} ON user_job_titles.user_id = users.id 
                    JOIN {add_prefix_for_prod('job_titles')} ON job_titles.id = user_job_titles.job_title_id 
                    JOIN {add_prefix_for_prod('user_industries')} ON user_industries.user_id = users.id 
                    JOIN {add_prefix_for_prod('industry_areas')} ON industry_areas.id = user_industries.industry_area_id
                    JOIN {add_prefix_for_prod('user_locations')} ON user_locations.user_id = users.id 
                    JOIN {add_prefix_for_prod('locations')} ON locations.id = user_locations.location_id
                    WHERE (connections.user_id = {id} OR connections.connected_id = {id}) 
                    AND job_titles.job_title = '{job_title[0]}' 
                    AND industry_areas.industry_area = '{industry_area[0]}' 
                    AND locations.city = '{location[0]}'
                    AND NOT users.id = {id}""")
        else:
            sql = text(f"""SELECT users.id
                    FROM {add_prefix_for_prod('users')}
                    JOIN {add_prefix_for_prod('connections')} on connections.connected_id = users.id 
                    JOIN {add_prefix_for_prod('user_job_titles')} ON user_job_titles.user_id = users.id 
                    JOIN {add_prefix_for_prod('job_titles')}  ON job_titles.id = user_job_titles.job_title_id 
                    JOIN {add_prefix_for_prod('user_industries')}  ON user_industries.user_id = users.id 
                    JOIN {add_prefix_for_prod('industry_areas')}  ON industry_areas.id = user_industries.industry_area_id
                    JOIN {add_prefix_for_prod('user_locations')}  ON user_locations.user_id = users.id 
                    JOIN {add_prefix_for_prod('locations')}  ON locations.id = user_locations.location_id
                    JOIN {add_prefix_for_prod('user_genres')} ON user_genres.user_id = users.id
                    JOIN {add_prefix_for_prod('genres')} ON genres.id = user_genres.genre_id
                    WHERE (connections.user_id = {id} OR connections.connected_id = {id}) 
                    AND job_titles.job_title = '{job_title[0]}' 
                    AND industry_areas.industry_area = '{industry_area[0]}' 
                    AND locations.city = '{location[0]}'
                    AND (genres.genre_name = '{genre[0]}')
                    AND NOT users.id = {id}""")

        result = db.session.execute(sql)
        query_results = result.all()
        """
        query results output:
        [(41, 'Elena', 'Santos', 'https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/lat-w/Slice+2.jpg'), (43, 'Gabriela', 'Uribe', 'https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/lat-w/Slice+7.jpg')]
        """

        """
        search_results = [{"id": user_id, "first_name": first_name, "last_name": last_name, "profile_img_url": profile_img_url} for user_id, first_name, last_name, profile_img_url in query_results]
        """
        search_results = []

        for idx in query_results:
            user = User.query.get(idx[0])
            search_results.append({
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "profile_img_url": user.profile_img_url,
                "bookings": [(booking.start_date, booking.end_date) for booking in user.bookings]
            })

        if len(search_results) == 0:
            return {"errors": "Sorry, none of your connections match this search."}, 404
        
        return search_results, 200
        """
        
        user = User.query.get(id)
        user_network = user.my_connections()
        # user_network are all the users the current user is connected to, whether by invitation sent or received

        request_data = request.json
        # .json turns request data into a dict

        # if a parameter is present add its filter to filter list, if not, add its anti-filter
        location_matched = filter(
            lambda user: location[0] in user["locations"], user_network
        )

        industry_matched = filter(
            lambda user: industry_area[0] in user["industry_areas"], location_matched
        )

        job_title_matched = filter(
            lambda user: job_title[0] in user["job_title"], industry_matched
        )
        # print(">>>>>> job_title_matched", list(job_title_matched))

        genre_matched = None

        if genre[0] != "None":

            genre_matched = filter(
                lambda user: genre[0] in user["genres"], job_title_matched
            )
        else:

            genre_matched = filter(
                lambda user: genre[0] not in user["genres"], job_title_matched
            )

        # ? filter object returns an iterable but not a list, so it has to be wrapped before sending

        search_results_lst = list(genre_matched)
        # ? this list comp removes duplicates from the list
        search_results = [
            i
            for n, i in enumerate(search_results_lst)
            if i not in search_results_lst[:n]
        ]

        if len(search_results) == 0:
            return {"errors": "Sorry, none of your connections match this search."}, 404

        
        return search_results, 200
        # ? Moved availability check to frontend for easier date object comparisons

    # print(">>>>>0form errors:", searchForm.errors)
    
    return searchForm.errors, 400
    """
    

# * CREATE CONNECTION
@connections_routes.route("/new", methods=["POST"])
def create_connection():

    connectionForm = NewConnectionsForm()
    connectionForm["csrf_token"].data = request.cookies["csrf_token"]

    request_data = request.json
    # .json turns request data into a dict

    initiator_id = request_data["user_id"]
    invitee_id = request_data["connected_id"]

    connection_type = connectionForm.data["connection_type"]
    connection_context = connectionForm.data["connection_context"]

    if connectionForm.validate_on_submit():
        try:

            newConnection = Connection(
                user_id=initiator_id,
                connected_id=invitee_id,
                connection_type=connection_type,
                connection_context=connection_context,
            )
            db.session.add(newConnection)
            db.session.commit()
            return {"message": "connection created successfully"}, 200
        
        except:
            return {"error": "There was a problem creating the connection"}, 500


    return {"error": new_connection_form.errors}, 400
