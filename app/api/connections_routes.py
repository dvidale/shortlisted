from flask import Blueprint, request
from app.models import User, db, Connection

connections_routes = Blueprint('connections', __name__)

@connections_routes.route('/<int:id>')
def search_connections(id):
    user = User.query.get(id)
    connections = user.connections_initiated
    # we need to write a query for all the Connections where the user_id or the connected_id on the connection matches our user_id

    user_network = [ User.query.get(connect.user_id).to_dict()  for connect in connections]
    print(">>>users", user_network)
    
    return connections
    