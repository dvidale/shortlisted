from flask import Blueprint, request
from app.models import db, Comment
from app.models.referral import Referral

comments_routes = Blueprint('comments', __name__)

@comments_routes.route('/<int:id>')
def get_comments(id):
    get_comments = db.session.scalars(
        db.select(Comment).where(Comment.referral_id == id)
    ).all()
    
    return [comment.to_dict() for comment in get_comments]