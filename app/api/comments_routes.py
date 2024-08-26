from flask import Blueprint, request
from app.models.referral import Referral

comments_routes = Blueprint('comments', __name__)

@comments_routes.route('/<int:id>')
def get_comments(id):
    pass