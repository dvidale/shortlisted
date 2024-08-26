from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField
from app.api.aws_utils import ALLOWED_EXTENSIONS

class SaveShortlistForm(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    description = TextAreaField('description')
    # TODO: Add image upload to form
    # optional_img = FileField("optional_img", validators=[FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))])
    # submit = SubmitField("Add Screenshot")