from flask_wtf import FlaskForm
from wtforms import StringField, ValidationError, SubmitField
from wtforms.validators import DataRequired


class BucketlistForm(FlaskForm):
    """Form for users to login"""
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Add')
