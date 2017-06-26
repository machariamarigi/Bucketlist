from flask_wtf import FlaskForm
from wtforms import StringField, ValidationError, SubmitField, DateField
from wtforms.validators import DataRequired


class BucketlistForm(FlaskForm):
    """Form used to create a bucketlist"""
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Add')


class BucketlistItem(FlaskForm):
    """Form used to create a bucketlist item"""
    item = StringField('Item', validators=[DataRequired()])
    due_date = StringField('DueDate', validators=[DataRequired()])
    submit = SubmitField('Add')
