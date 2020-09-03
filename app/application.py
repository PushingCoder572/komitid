"""
Created on 2020-08-27
Fläsk
Project: komitid
@author: ollejernstrom
"""

# Libraries and frameworks
from flask import Flask, g, render_template, redirect, request, url_for, session

from app.models import checkuser,get_data, get_session_user, db_query, create_user

# Setup
app = Flask(__name__)
app.secret_key = 'ennyckeljävelbarajagkan'


@app.before_request
def before_request():
    if 'user_id' in session:
        user = get_session_user(session['user_id'])
        g.user = user


@app.route('/home')
def home():
    print(g.user.id)
    return render_template('sites/home.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        re_password = request.form.get('re_password')
        existing_usernames = db_query('name')

        if username not in existing_usernames and password == re_password:
            create_user(username, password)
            print('User Created')
            return redirect(url_for('login'))
        print('Could not create account')

    return render_template('sites/signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('user_id', None)  # Removes existing user

        # Gets form data
        uname = request.form.get('username')
        pword = request.form.get('password')

        # Checks if user exists
        userid = checkuser(uname, pword)
        if userid:
            session['user_id'] = userid
            return redirect(url_for('home'))

        # flash an Error msg
        return redirect(url_for('login'))

    return render_template('sites/login.html')


@app.route('/')
def index():
    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)
