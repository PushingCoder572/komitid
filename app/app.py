"""
Created on 2020-08-27
Fläsk
Project: komitid
@author: ollejernstrom
"""

from flask import request, render_template, Flask
from app.models import create_user

app = Flask(__name__)


@app.route('/signup', methods=['POST'])
def mypage():
    if request.method == 'POST':
        uname = request.form.get('uname')
        pword = request.form.get('pword')
        create_user(uname, pword)


@app.route('/', methods=['GET', 'POST'])
def home():
    uname = request.form.get('uname')
    pword = request.form.get('pword')
    create_user(uname, pword)

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
