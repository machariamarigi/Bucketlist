"""Module handle authentification views"""

from flask import render_template

from . import auth


@auth.route('/login')
def login():
    """Method to handle views for loging in"""
    return render_template('auth/login.html', title='login')
