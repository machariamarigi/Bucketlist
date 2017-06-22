from flask_wtf import FlaskForm
from wtforms import StringField, ValidationError, SubmitField
from wtforms.validators import DataRequired


class BucketlistForm(FlaskForm):
    """Form for users to login"""
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Add')
