from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, SubmitField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired, Length


class ProfileInfoForm(FlaskForm):
    phone_number = StringField('phone_number', validators=[Length(max=20)])
    profile_img_url = StringField('profile_img_url', validators=[Length(max=255)])
   
    industry_area = SelectMultipleField('industry_area', validators=[DataRequired()], choices=['Scripted Television', 'Unscripted Television', 'Dramatic Film', 'Documentary', 'Commercial'])
    job_title = SelectMultipleField('job_title', validators=[DataRequired()], choices=['Editor','Assistant Editor'])
    genre = SelectMultipleField('genre', choices=['None','Drama','Comedy','Horror','Sci-Fi','Animation', 'Historical'])
    location = SelectMultipleField('location',validators=[DataRequired()], choices=['Atlanta', 'Los Angeles', 'New York', 'Remote'])   
