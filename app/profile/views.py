""" Module for handling profile blueprint views"""

from flask import render_template

from . import profile


@profile.route('/profile')
def profilepage():
    """Render the homepage template on the / route"""
    return render_template('profile/profile.html')
