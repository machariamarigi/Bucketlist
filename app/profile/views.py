""" Module for handling profile blueprint views"""

from flask import render_template, session

from . import profile
# from .forms import BucketlistForm
from ..models import BucketList


@profile.route('/profile', methods=['GET', 'POST'])
def profilepage():
    """Render the homepage template on the / route"""
    if session['logged_in']:
        user = session['username']
        return render_template('profile/profile.html', user=user)
    else:
        return render_template('401.html')
