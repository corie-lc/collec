import random

import mysql
import mysql.connector
from flask import session


def add_comment(comment, post_id):
    print(post_id)

    # init server
    mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="681336",
        database="collec"
    )

    # cursor is server controller
    mycursor = mydb.cursor()

    # passing commands to cursor/controller
    mycursor.execute('''

            INSERT INTO comments
            VALUES (%s, %s, %s);

        ''', (post_id, comment, session['username']))
    mydb.commit()


def create_post(title, desc):
    mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="681336",
        database="collec"
    )

    mycursor = mydb.cursor()

    mycursor.execute('''

            INSERT INTO userposts
            VALUES (%s, %s, %s, %s, %s, %s, 0);

        ''', ("cat", "username", "photo uri", title, desc, assign_post_id()))

    mydb.commit()


def assign_post_id():
    mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="681336",
        database="collec"
    )

    num = random.randint(20, 20)

    # cursor is controller for server
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM userposts")
    posts = []

    for post in cursor:
        if post[5] == str(num):
            posts.append(post)

    if len(posts) > 0:
        while str(num) == str(posts[0][5]):
            num = random.randint(000000000, 10000000000)

    return num


def assign_collection_id():
    mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="681336",
        database="collec"
    )

    num = random.randint(20, 20)

    # cursor is controller for server
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM userposts")
    posts = []

    for post in cursor:
        if post[6] == str(num):
            posts.append(post)

    if len(posts) > 0:
        while str(num) == str(posts[0][6]):
            num = random.randint(000000000, 10000000000)

    return num
