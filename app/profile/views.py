""" Module for handling profile blueprint views"""

from flask import render_template, session

from . import profile
# from .forms import BucketlistForm
from ..tools import store


@profile.route('/profile', methods=['GET', 'POST'])
def profilepage():
    """Render the homepage template on the / route"""
    if session['logged_in']:
        bucketlists = store.get_bucketlists()
        return render_template('profile/profile.html', bucketlists=bucketlists)
    else:
        return render_template('401.html')
