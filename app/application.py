"""
Created on 2020-08-27
Fläsk
Project: komitid
@author: ollejernstrom
"""

from flask import request, render_template, Flask, url_for, redirect
from app.models import create_user, checkuser


app = Flask(__name__)


@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('sites/home.html')



@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        uname = request.form.get('username')
        pword = request.form.get('password')
        pword_confrimation = request.form.get('re_password')
        if uname and pword and pword_confrimation:
            if pword == pword_confrimation:
                create_user(uname, pword)
                print('Created user', uname, pword)
                return render_template('sites/signup.html', status='User Created!')

            return render_template('sites/signup.html', status='Wrong inputs')

    return render_template('sites/signup.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uname = request.form.get('username')
        pword = request.form.get('password')
        if uname and pword:
            if checkuser(uname, pword):
                return redirect('/home')
        return render_template('layout.html', failed='The username does not match the password!')




    return render_template('layout.html')


if __name__ == '__main__':
    app.run(debug=True)