from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, DateTimeField
from wtforms.validators import DataRequired, ValidationError

# TODO: refactor all these choices lists to be dynamically populated

class SearchConnectionsForm(FlaskForm):

    location = SelectMultipleField('location',validators=[DataRequired()], choices=['Atlanta', 'Los Angeles', 'New York', 'Remote'])   
    industry_area = SelectMultipleField('industry_area', validators=[ DataRequired()], choices=['Scripted Television', 'Unscripted Television', 'Dramatic Film', 'Documentary', 'Commercial'])
    job_title = SelectMultipleField('job_title', validators=[DataRequired()], choices=['Editor','Assistant Editor'])
    genre = SelectMultipleField('genre', choices=['None','Drama','Comedy','Horror','Sci-Fi','Animation', 'Historical'])

    # ? start and end date search params are being evaluated purely on the frontend. keeping for future options - 08/27/2024
    # start_date = DateTimeField('start_date', validators=[DataRequired()])
    # end_date = DateTimeField('end_date')

