from flask import Flask, render_template, redirect, session, request
from flask_app.models import chore
from flask_app import app


# create chore controller
@app.route('/chores/create')
def create_page():
    if 'user_id' not in session: return redirect('/')
    return render_template('create_chore.html')

@app.post('/chores/create')
def create_chore():
    if 'user_id' not in session: return redirect('/')
    if chore.Chore.create_chore(request.form):
        return redirect('/chores')
    return redirect('/chores/create')


# read chore controller
@app.route('/chores/view/<int:id>')
def view_chores(id):
    if 'user_id' not in session: return redirect('/')
    this_chore = chore.Chore.get_chore_by_id_w_host(id)
    return render_template('chore_details.html', chore = this_chore)


# update chore controller
@app.route('/chores/edit/<int:id>')
def edit_page(id):
    if 'user_id' not in session: return redirect('/')
    this_chore = chore.Chore.get_chore_by_id_w_host(id)
    return render_template('edit_chore.html', chore = this_chore)

@app.post('/chores/edit')
def edit_chore():
    if 'user_id' not in session: return redirect('/')
    if chore.Chore.update_chore(request.form):
        return redirect('/chores')
    return redirect(f'/chores/edit/{request.form["id"]}')

# delete chore controller

@app.route('/chores/delete/<int:id>')
def delete_chore(id):
    if 'user_id' not in session: return redirect('/')
    chore.Chore.delete_chore_by_id(id)
    return redirect('/chores')


