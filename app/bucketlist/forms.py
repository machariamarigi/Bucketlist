from flask_wtf import FlaskForm
from wtforms import StringField, ValidationError, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class BucketlistForm(FlaskForm):
    """Form used to create a bucketlist"""
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Add')


class BucketlistItemForm(FlaskForm):
    """Form used to create a bucketlist item"""
    item = StringField('Item', validators=[DataRequired()])
    due_date = DateField(
        'DueDate', validators=[DataRequired()], format='%Y-%d-%m')
    submit = SubmitField('Add')
