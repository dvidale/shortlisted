from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Length
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField
from app.api.aws_utils import ALLOWED_EXTENSIONS
from app.models.shortlist import Shortlist

class SaveShortlistForm(FlaskForm):
    title = StringField('title', validators=[ DataRequired(message="A title is required"), Length(max=50)])
    description = TextAreaField('description',validators=[Length(max=255)] )
    # TODO: Add image upload to form
    # optional_img = FileField("optional_img", validators=[FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))])
    # submit = SubmitField("Add Screenshot")