"""Module handle authentification views"""

from flask import render_template, flash, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash


from . import auth
from .forms import SignUpForm, LoginForm
from ..models import User


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """Method to handle views for loging in"""
    form = LoginForm()
    if form.validate_on_submit():

        if form.email.data == session['email']:
            # hash_password = generate_password_hash(form.password.data)
            # chech_hash = check_password_hash(session['password'], form.email.data)
            if form.password.data == session['password']:
                return redirect(url_for('profile.profilepage'))

    return render_template('auth/login.html', title='login', form=form)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    """Method to handle sign up of users"""
    form = SignUpForm()
    if form.validate_on_submit():
        # TODO: Hash passwords
        # hash_password = generate_password_hash(form.password.data)
        new_user = User(
            form.username.data, form.email.data, form.password.data)
        user_details = new_user.get_details()

        session['email'] = user_details['email']
        session['password'] = user_details['password']
        session['username'] = user_details['username']
        flash('You have successfully registered! You may now login.')
        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html', form=form, title='Sign Up')


@auth.route('/logout')
def logout():
    [session].clear()
    return redirect(url_for('home.homepage'))
