from flask import Blueprint, request
from app.models import db, Comment
from app.models.referral import Referral
from app.forms.comment_form import CommentForm

comments_routes = Blueprint('comments', __name__)


#  * GET COMMENTS BY REFERRAL ID

@comments_routes.route('/<int:id>')
def get_comments(id):
    get_comments = db.session.scalars(
        db.select(Comment).where(Comment.referral_id == id)
    ).all()
    
    return [comment.to_dict() for comment in get_comments]

# * CREATE A NEW COMMENT

@comments_routes.route('/new', methods=['POST'])
def add_comment():
    comment_form = CommentForm()

    comment_form["csrf_token"].data = request.cookies["csrf_token"]

    text = comment_form.data['text']

    if comment_form.validate_on_submit():
        request_data = request.json
        # .json turns request data into a dict

        shortlist_id = request_data['shortlist_id']
        commenter_id = request_data['commenter_id']
        referral_id = request_data['referral_id']

        newComment = Comment(
            shortlist_id = shortlist_id,
            commenter_id = commenter_id,
            referral_id = referral_id,
            text = text
        )

        db.session.add(newComment)
        db.session.commit()

        newCommentFromDB = db.session.scalars(
            db.select(Comment).filter(Comment.commenter_id == commenter_id).where(Comment.referral_id == referral_id).order_by(Comment.createdAt.desc())
        ).first()

        return newCommentFromDB.to_dict()
    
    return {"error": comment_form.errors}


# * UPDATE A COMMENT

@comments_routes.route('/<int:id>', methods=['PUT'])
def update_comment(id):
     comment_form = CommentForm()

     comment_form["csrf_token"].data = request.cookies["csrf_token"]

     text = comment_form.data['text']

     if comment_form.validate_on_submit():
        target_comment = Comment.query.get(id)

        target_comment.text = text

        db.session.commit()

        return target_comment.to_dict()
     
     return {"error": comment_form.errors}

# * DELETE A COMMENT

@comments_routes.route('/<int:id>', methods=['DELETE'])
def delete_comment(id):
    target_comment = Comment.query.get(id)

    db.session.delete(target_comment)
    db.session.commit()

    return {"message" : "Comment deleted"}