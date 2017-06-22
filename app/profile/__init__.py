""" Blueprint for a user's profile page"""
from flask import Blueprint

profile = Blueprint('profile', __name__)

from . import views
