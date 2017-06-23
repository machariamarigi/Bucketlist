""" Blueprint for our app's homepage"""

from flask import Blueprint

bucketlist = Blueprint('bucketlist', __name__)

from . import views
