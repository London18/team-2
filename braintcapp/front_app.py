from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import sqlite3
import numpy as np
import os
from flask import abort, redirect, url_for


# app = Flask(__name__)

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

class ReusableForm(Form):
    name = TextField('What you want to search:', validators=[validators.required()])


@app.route('/home')
def home():
    if not session.get('logged_in'):
        return render_template('home.html')
    else:
        return "Hello Boss!"

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()

@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)

    print (form.errors)
    if request.method == 'POST':
        name=request.form['name']
        print (name)

        if form.validate():
            # Save the comment here.
            flash('Hello ' + name)
        else:
            flash('All the form fields are required. ')

        if name == "sympton":
            return render_template('symptom.html')


    return render_template('hello.html', form=form)

@app.route('/sympton', methods=['GET','POST'])
def getlinks():
    con = sqlite3.connect('../db/knowledge_base.db')
    c = con.cursor()
    # sql2 = ""
    sql = "SELECT * FROM knowledge where category_id = (select category_id from category where category_name = 'symptons')"
    c.execute(sql)
    k3 = c.fetchall()
    render_string = '<ul>'

    for i in k3:
        k2 = np.array(i)

        render_string += '<li><a href="'+k2[1]+'">' + k2[1] + '</ a></li>'

    render_string += '</ul>'

    return render_string



# @app.route("/base", methods=['GET', 'POST'])
# def base():
#     return render_template('base.html')
#
# @app.route("/base/register", methods=['GET', 'POST'])
# def register():
#     return render_template('register.html')
#
# @app.route("/base/login", methods=['GET', 'POST'])
# def login():
#     return render_template('login.html')

if __name__ == "__main__":
    # app.secret_key = os.urandom(12)
    # app.run(debug=True,host='0.0.0.0', port=4000)
    app.run()