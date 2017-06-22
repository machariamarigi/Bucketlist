""" Module for handling profile blueprint views"""

from flask import render_template, session

from . import profile
# from .forms import BucketlistForm
from ..models import BucketList


@profile.route('/profile')
def profilepage():
    """Render the homepage template on the / route"""

    user = session['username']
    return render_template('profile/profile.html', user=user)


# @profile.route('/create_bucketlist', methods=['GET', 'POST'])
# def create_bucketlist():
    
