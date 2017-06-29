"""Module to handle views for  CRUD operation on our bucket list"""

from flask import render_template, flash, redirect, url_for, session

from . import bucketlist
from .forms import BucketlistForm, BucketlistItemForm
from ..tools import store


@bucketlist.route('/bucketlist/add', methods=['GET', 'POST'])
def add_bucketlist():
    """Render a form to handle the creation of bucketlists"""
    if session['logged_in']:
        add_bucketlist = True
        form = BucketlistForm()
        if form.validate_on_submit():
            store.add_bucketlist(form.title.data, form.description.data)
            flash('You have succesfully created {} bucketlist'.format(
                form.title.data))

            return redirect(url_for('profile.profilepage'))
        return render_template(
            "bucketlist/add_bucketlist.html",
            form=form, add_bucketlist=add_bucketlist)
    else:
        render_template('401.html')


@bucketlist.route('/bucketlist/<id>', methods=['GET', 'POST'])
def view_bucketlist(id):
    if session['logged_in']:
        view_bucketlist = store.get_single_bucketlist(int(id))
        items = view_bucketlist['items']
        return render_template(
            "bucketlist/bucketlist.html",
            bucketlist=view_bucketlist,
            items=items
            )


@bucketlist.route('/bucketlist/edit/<id>', methods=['GET', 'POST'])
def edit_bucketlist(id):
    if session['logged_in']:
        add_bucketlist = False
        single_bucketlist = store.get_single_bucketlist(int(id))
        form = BucketlistForm(dict=single_bucketlist)
        if form.validate_on_submit():
            single_bucketlist['title'] = form.title.data
            single_bucketlist['description'] = form.description.data
            return redirect(url_for('profile.profilepage'))
        form.title.data = single_bucketlist['title']
        form.description.data = single_bucketlist['description']
        return render_template(
            "bucketlist/add_bucketlist.html",
            form=form, add_bucketlist=add_bucketlist)
    else:
        render_template('401.html')


@bucketlist.route('/bucketlist/delete/<id>', methods=['GET', 'POST'])
def delete_bucketlist(id):
    if session['logged_in']:
        store.remove_bucketlist(int(id))
        return redirect(url_for('profile.profilepage'))
        return render_template(title="Delete Bucketlist")
    else:
        render_template('401.html')


@bucketlist.route('/bucketlist_item/add/<id>', methods=['GET', 'POST'])
def add_bucketlist_item(id):
    """Render a form to handle the creation of bucketlist goals"""
    if session['logged_in']:
        add_bucketlist_item = True
        view_bucketlist = store.get_single_bucketlist(int(id))
        form = BucketlistItemForm()
        if form.validate_on_submit():
            store.add_bucketlist_item(
                int(id),
                form.item.data,
                form.due_date.data
            )
            flash('You have succesfully created {} goal'.format(
                form.item.data)
            )
            return redirect(url_for('bucketlist.view_bucketlist', id=id))
        return render_template(
            "bucketlist/add_bucketlist_item.html",
            form=form,
            add_bucketlist_item=add_bucketlist_item,
            bucketlist=view_bucketlist
        )
    else:
        render_template('401.html')


@bucketlist.route('/bucketlis_item/edit/<b_id>/<bi_id>', methods=['GET', 'POST'])
def edit_bucketlist_item(b_id, bi_id):
    if session['logged_in']:
        add_bucketlist_item = False
        single_bucketlist = store.get_bucketlist_item(int(b_id), int(bi_id))
        form = BucketlistItemForm(dict=single_bucketlist)
        if form.validate_on_submit():
            single_bucketlist['item'] = form.item.data
            single_bucketlist['duedate'] = form.due_date.data
            return redirect(url_for('bucketlist.view_bucketlist', id=b_id))
        form.item.data = single_bucketlist['item']
        form.due_date.data = single_bucketlist['duedate']
        return render_template(
            "bucketlist/add_bucketlist.html",
            form=form, add_bucketlist_item=add_bucketlist_item)
    else:
        render_template('401.html')


@bucketlist.route('/bucketlist/delete/<b_id>/<bi_id>', methods=['GET', 'POST'])
def delete_bucketlist_item(b_id, bi_id):
    if session['logged_in']:
        store.remove_bucketlist_item(int(b_id), int(bi_id))
        return redirect(url_for('bucketlist.view_bucketlist', id=b_id))
        return render_template(title="Delete Bucketlist Item")
    else:
        render_template('401.html')
