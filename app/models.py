"""
Created on 2020-08-27

Purpose: Interacts with the database
Project: komitid
@author: ollejernstrom
"""

"""
Created on 2020-08-25

Project: social
@author: ollejernstrom
"""
import sqlite3 as sql
from os import path

ROOT = path.dirname(path.realpath(__file__))


def create_user(uname, pword):
    connection = sql.connect(path.join(ROOT, 'database.db'))
    cursor = connection.cursor()
    cursor.execute('insert into users (name, content) values(?, ?)', (uname, pword))
    connection.commit()
    connection.close()



def get_posts():
    connection = sql.connect(path.join(ROOT, 'database.db'))
    cursor = connection.cursor()
    cursor.execute('select * from posts')
    posts = cursor.fetchall()
    return posts
