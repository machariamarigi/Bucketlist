""" Module for handling home blueprint views"""

from flask import render_template, session

from . import home


@home.route('/')
def homepage():
    """Render the homepage template on the / route"""
    session['logged_in'] = False
    return render_template('home/index.html')


@home.route('/about')
def about():
    """Render the homepage template on the /about route"""
    return render_template('home/about.html')
