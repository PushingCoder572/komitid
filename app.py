"""
Created on 2020-08-27

Project: komitid
@author: ollejernstrom
"""

from flask import request, render_template, Flask

app = Flask(__name__)


@app.route('/')
def dash():
    return render_template()
