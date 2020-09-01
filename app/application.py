"""
Created on 2020-08-27
Fläsk
Project: komitid
@author: ollejernstrom
"""

# Libraries and frameworks
from flask import Flask, render_template, redirect, request
from app.models import checkuser


# Setup
app = Flask(__name__)


@app.route('/signup')
def signup():
    return render_template('sites/signup.html')


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form.get('username')
        pword = request.form.get('password')
        if uname and pword:
            if checkuser(uname, pword):
                return redirect('/home')
        return render_template('login.html')
    return render_template('sites/login.html')


@app.route('/')
def index():
    return redirect('/login')




if __name__ == '__main__':
    app.run(debug=True)