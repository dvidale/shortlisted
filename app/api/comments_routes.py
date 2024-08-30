from flask import Blueprint, request
from app.models import db, Comment
from app.models.referral import Referral
from app.models.user import User
from app.models.shortlist import Shortlist
from app.forms.comment_form import CommentForm

comments_routes = Blueprint('comments', __name__)


#  * GET ALL COMMENT THREADS BY USER ID

@comments_routes.route('/<int:id>')
def get_comments(id):
    current_user = User.query.get(id)
    user_shortlists = current_user.shortlists

    referral_lst = [
    db.session.scalars(
        db.select(Referral).where(Referral.shortlist_id == shortlist.id)
    ).all() for shortlist in user_shortlists]

    referrals_unnested = [ x for xs in referral_lst for x in xs ]

    comment_threads = [ referral.comments for referral in referrals_unnested ]

    # for each nested list of comments, go into that list, and apply to_dict to each comment

    threads_unpacked = list(map(lambda thread: [comment.to_dict() for comment in thread], comment_threads))
    
    nonempty_threads = list(filter(lambda thread: len(thread) > 0, threads_unpacked))
    # print(">>>>>>nonempty_threads", nonempty_threads)
    return nonempty_threads

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
    
    return {"error": comment_form.errors}, 400


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

        updatedComment = db.session.scalars(
            db.select(Comment).where(Comment.id == target_comment.id)
        ).first()

        return updatedComment.to_dict()
     
     return {"error": comment_form.errors}, 400

# * DELETE A COMMENT

@comments_routes.route('/<int:id>', methods=['DELETE'])
def delete_comment(id):
    target_comment = Comment.query.get(id)

    target_referral_id = target_comment.to_dict()['referral_id']

    db.session.delete(target_comment)
    db.session.commit()

   
    # fresh_lst = db.session.scalars(
    #         db.select(Comment).where(Comment.referral_id == target_comment.referral_id)
    #     ).all()
    # # ? send back the entire list with the comment removed
    # return [comment.to_dict() for comment in fresh_lst]
    return {"target_thread" : target_referral_id}, 200