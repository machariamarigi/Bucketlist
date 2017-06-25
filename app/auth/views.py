"""Module handle authentification views"""

from flask import render_template, flash, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash


from . import auth
from .forms import SignUpForm, LoginForm
from ..tools import store


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """Method to handle views for loging in"""
    form = LoginForm()
    if form.validate_on_submit():
        for user in store.users:
            if form.email.data == user['email']:
                if form.password.data == user['password']:
                    logged_in_user = user
                    session['logged_in'] = True
                    return redirect(
                        url_for(
                            'profile.profilepage',
                            logged_in_user=logged_in_user['username']))
                else:
                    flash('Ensure that you are a registered user')
            else:
                flash('Ensure that you are a registered user')

    return render_template('auth/login.html', title='login', form=form)


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    """Method to handle sign up of users"""
    form = SignUpForm()
    if form.validate_on_submit():
        # TODO: Hash passwords
        # hash_password = generate_password_hash(form.password.data)
        store.add_user(form.username.data, form.email.data, form.password.data)
        flash('You have successfully registered! You may now login.')
        return redirect(url_for('auth.login'))
    return render_template('auth/signup.html', form=form, title='Sign Up')


@auth.route('/logout')
def logout():
    """Log out a user"""
    session.pop('email', None)
    session.pop('password', None)
    session.pop('username', None)
    session.pop('logged_in', None)
    return redirect(url_for('home.homepage'))
