"""Module to handle views for  CRUD operation on our bucket list"""

from flask import render_template, flash, redirect, url_for, session

from . import bucketlist
from .forms import BucketlistForm
from ..tools import store


@bucketlist.route('/bucket_list/add', methods=['GET', 'POST'])
def add_bucketlist():
    """Render a form to handle the creation of bucketlists"""
    if session['logged_in']:
        form = BucketlistForm()
        if form.validate_on_submit():
            store.add_bucketlist(form.title.data, form.description.data)
            flash('You have succesfully created {} bucketlist'.format(
                form.title.data))

            return render_template(
                'profile/profile.html',
                bucketlists=store.get_bucketlists())
        return render_template("bucketlist/add_bucketlist.html", form=form)
    else:
        render_template('401.html')


@bucketlist.route('/bucket_list/<id>', methods=['GET', 'POST'])
def view_bucketlist(id):
    if session['logged_in']:
        return render_template("bucketlist/bucketlist.html")
