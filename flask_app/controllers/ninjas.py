from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from pprint import pprint


@app.route('/new_ninja')
def new_ninja_page():
    dojos = Dojo.get_all_dojos()
    return render_template('new_ninja.html', dojos=dojos)

@app.post('/new_ninja')
def create_ninja():
    data = {
        'dojo_id': request.form['dojo_id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }
    Ninja.create_ninja(data)
    pprint(data)
    return redirect('/')

