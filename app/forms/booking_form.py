from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class BookingForm(FlaskForm):
    user_id = IntegerField('user_id')
    shortlist_id = IntegerField('shortlist_id')
    start_date = StringField('start_date', validators=[DataRequired(message='A start date is required')])
    end_date = StringField('end_date',validators=[DataRequired(message='An end date is required')] )