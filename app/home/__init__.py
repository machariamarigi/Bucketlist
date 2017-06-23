""" Blueprint for our app's homepage"""
from flask import Blueprint

home = Blueprint('home', __name__)

from . import views
