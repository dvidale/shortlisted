from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField

from wtforms.validators import DataRequired, Email, ValidationError, Length, EqualTo, InputRequired
from app.api.aws_utils import ALLOWED_EXTENSIONS

from app.models import User


def user_exists(form, field):
    # Checking if user exists
    email = field.data
    user = User.query.filter(User.email == email).first()
    if user:
        raise ValidationError("Email address is already in use.")


def username_exists(form, field):
    # Checking if username is already in use
    username = field.data
    user = User.query.filter(User.username == username).first()
    if user:
        raise ValidationError("Username is already in use.")


class SignUpForm(FlaskForm):
    first_name = StringField(
        "first_name", validators=[DataRequired(), Length(min=2, max=225)]
    )

    last_name = StringField(
        "last_name", validators=[DataRequired(), Length(min=2, max=225)]
    )

    email = StringField(
        "email", validators=[DataRequired(), user_exists, Length(min=6, max=50), Email(message="Must be a valid email address")]
    )

    username = StringField(
        "username", validators=[DataRequired(), username_exists, Length(min=6)]
    )

    password = PasswordField(
        "password",
        validators=[
            InputRequired(),
            EqualTo("confirmPassword", message="Passwords must match"),
            Length(min=8),
        ],
    )

    confirmPassword = PasswordField("confirm")
