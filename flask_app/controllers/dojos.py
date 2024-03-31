from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    dojos = Dojo.get_all_dojos()
    print(dojos)
    return render_template('index.html', dojos=dojos)


@app.route('/dojoshow/<int:dojo_id>')
def dojoshow(dojo_id):
    dojos = Dojo.get_one_dojo(dojo_id)
    ninjas = Dojo.get_dojo_ninjas(dojo_id)
    print(dojos)
    return render_template('dojoshow.html', dojos=dojos, ninjas=ninjas)

@app.post('/create_dojo')
def create_dojo():
    data = {'name': request.form['name']}
    Dojo.create_dojo(request.form)
    return redirect('/')


