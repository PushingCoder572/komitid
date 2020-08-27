"""
Created on 2020-08-27
Fläsk
Project: komitid
@author: ollejernstrom
"""

from flask import request, render_template, Flask, url_for
from app.models import create_user

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        uname = request.form.get('new_uname')
        pword = request.form.get('new_pword')
        pword_confrimation = request.form.get('repeat_pword')
        if pword == pword_confrimation:
            create_user(uname, pword)

    return render_template('sites/signup.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uname = request.form.get('uname')
        pword = request.form.get('pword')



    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)