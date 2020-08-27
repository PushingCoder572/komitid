"""
Created on 2020-08-27
Fläsk
Project: komitid
@author: ollejernstrom
"""

from flask import request, render_template, Flask, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    print(url_for('static', filename="css/style.css"))
    print(url_for('static', filename="js/script.js"))
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)