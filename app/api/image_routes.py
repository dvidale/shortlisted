from flask import Blueprint, request, redirect, render_template
from app.models import db
from flask_login import current_user, login_required
from app.api.aws_utils import (
    upload_file_to_s3, get_unique_filename)
from app.forms import ImageForm
from app.models import User

image_routes = Blueprint("images", __name__)


@image_routes.route("/new", methods=["POST"])
@login_required
def upload_image():
    form = ImageForm()

    form["csrf_token"].data = request.cookies["csrf_token"]
 
    if form.validate_on_submit():
          
        image = form.data["image"]
        image.filename = get_unique_filename(image.filename)
       
        upload = upload_file_to_s3(image)
        print(upload)

        if "url" not in upload:
        # if the dictionary doesn't have a url key
        # it means that there was an error when we tried to upload
        # so we send back that error message (and we printed it above)
            return upload

        url = upload["url"]
        return upload

    if form.errors:
        print(form.errors)
        return form.errors

    return {"message":"your submission was invalid"}