"""Module handle authentification views"""

from flask import render_template, flash, redirect, url_for

from . import auth
from ..tools import Auth

from .forms import SignUpForm, LoginForm


@auth.route('/login')
def login():
    """Method to handle views for loging in"""
    return render_template('auth/login.html', title='login')


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    """Method to handle sign up of users"""
    form = SignUpForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        auth = Auth()
        auth.signup(email, password)
        flash('You have successfully registered! You may now login.')
        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html', form=form, title='Sign Up')
