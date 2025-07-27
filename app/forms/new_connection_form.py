from flask_wtf import FlaskForm
from wtforms import SelectMultipleField, StringField
from wtforms.validators import DataRequired, Length

class NewConnectionsForm(FlaskForm):

    connection_type = SelectMultipleField('connection_type', validators=[DataRequired()], choices=['Familiar with their work', 'Worked together'])
    connection_context = StringField('connection_context', validators=[DataRequired(), Length(min=2, max=100) ])