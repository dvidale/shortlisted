from flask import Blueprint, request
from app.forms import new_connection_form
from app.models import User, db, Connection
from app.forms.search_connections_form import SearchConnectionsForm
import json
from dateutil import parser
from app.forms.new_connection_form import NewConnectionsForm

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
