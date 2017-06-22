"""Module to handle views for  CRUD operation on our bucket list"""

from flask import render_template, flash, redirect, url_for

from . import bucketlist
from .forms import BucketlistForm


@bucketlist.route('/bucket_list/add')
def add_bucketlist():
    form = BucketlistForm()
    return render_template("bucketlist/add_bucketlist.html", form=form)


