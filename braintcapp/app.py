
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from flask import Flask, request, redirect, url_for, render_template, session, abort,flash
import sqlite3
import numpy as np
app = Flask(__name__)
app.secret_key = 'some secret key'

books = ['the first book', 'the second book', 'the third book']
con = sqlite3.connect('../db/knowledge_base.db')
c = con.cursor()
c.execute("SELECT * FROM category")
knowledge = c.fetchall()

class ReusableForm(Form):
    name = TextField('What you want to search:', validators=[validators.required()])


@app.route('/home')
def home():
    if not session.get('logged_in'):
        return render_template('home.html')
    else:
        return "Hello Boss!"

@app.route('/Adddata', methods=['GET','POST'])
def Add_data():

    return render_template('Adddata.html')

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
            return render_template('home.html')


    return render_template('hello.html', form=form)


@app.route("/category")
def index():
    render_string = '<ul>'

    for book in knowledge:
        k2 = np.array(book)
        render_string += '<li><a href="/select?cato='+k2[0]+'">' + str(k2[1]) + '</a></li>'

    render_string += '</ul>'

    return render_string

@app.route("/select",methods=['GET'])
def select():
    getcato= request.args.get('cato');
    # print(getcato)
    con = sqlite3.connect('../db/knowledge_base.db')
    c = con.cursor()

    sql = "SELECT * FROM knowledge where category_id="+getcato
    print(sql)
    c.execute(sql)
    k3 = c.fetchall()
    render_string = '<ul>'

    for i in k3:
        k2 = np.array(i)

        render_string += '<li><a href="/select2?kn='+k2[1]+'">' + k2[1] + '</a></li>'

    render_string += '</ul>'

    return render_string

@app.route("/select2",methods=['GET'])
def select2():
    getkn= request.args.get('kn');
    # print(getcato)
    con = sqlite3.connect('../db/knowledge_base.db')
    c = con.cursor()

    sql = "SELECT * FROM knowledge where knowledge_name='"+getkn+"'"
    print(sql)
    c.execute(sql)
    k3 = c.fetchall()
    print(222)
    render_string = '<ul>'

    for i in k3:
        k2 = np.array(i)
        print(i)

        render_string += '<li>'+ k2[2] + '</li>'

    render_string += '</ul><div>DO YOU THINK IT IS USEFUL?</div>'

    return render_string



@app.route("/book", methods=['POST', 'GET'])
def book():
    _form = request.form

    if request.method == 'POST':
        title = _form["title"]
        books.append(title)
        return redirect(url_for('index'))

    return '''
        <form name="book" action="/book" method="post">
            <input id="title" name="title" type="text" placeholder="add book">
            <button type="submit">Submit</button>
        </form>
        '''

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5200, debug=True)