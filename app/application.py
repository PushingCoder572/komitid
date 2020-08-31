"""
Created on 2020-08-27
Fläsk
Project: komitid
@author: ollejernstrom
"""

# Libraries and frameworks
from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy


# Setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'



@app.route('/signup')
def signup():
    return render_template('sites/signup.html')



@app.route('/login')
def login():
    print(User.query.all())
    return render_template('sites/login.html')

@app.route('/')
def index():
    return redirect('/login')



if __name__ == '__main__':
    app.run(debug=True)