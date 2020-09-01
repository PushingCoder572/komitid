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
from app.errors import ServerError

ROOT = path.dirname(path.realpath(__file__))


def create_user(uname, pword):
    connection = sql.connect(path.join(ROOT, 'database.db'))
    cursor = connection.cursor()
    cursor.execute('insert into users (name, password) values(?, ?)', (uname, pword))
    connection.commit()
    connection.close()


def get_posts():
    connection = sql.connect(path.join(ROOT, 'database.db'))
    cursor = connection.cursor()
    cursor.execute('select * from users')
    posts = cursor.fetchall()
    return posts


def delete_user(uname):
    connection = sql.connect(path.join(ROOT, 'database.db'))
    cursor = connection.cursor()
    cursor.execute('delete from users where name=?', (uname,))
    connection.commit()
    connection.close()


def checkuser(try_uname, try_pword):
    valid_users = get_posts()
    if valid_users:
        for db_id, uname, pword in valid_users:
            if try_uname == uname and try_pword == pword:
                print(True)
                return True

        return False

    raise ServerError
