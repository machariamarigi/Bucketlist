"""Module to handle views for  CRUD operation on our bucket list"""

from flask import render_template, flash, redirect, url_for

from . import bucketlist
from .forms import BucketlistForm
from ..models import BucketList


@bucketlist.route('/bucket_list/add', methods=['GET', 'POST'])
def add_bucketlist():
    """Render a form to handle the creation of bucketlists"""
    form = BucketlistForm()
    if form.validate_on_submit():
        bucketlist = BucketList()
        bucketlist.create_bucketlist(form.title.data, form.description.data)
        flash('You have succesfully created {} bucketlist'.format(
            form.title.data))

        return render_template(
            'profile/profile.html',
            bucketlists=bucketlist.get_bucketlists())
    return render_template("bucketlist/add_bucketlist.html", form=form)
