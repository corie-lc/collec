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
            VALUES (%s, %s, %s, %s, %s);

        ''', ("cat", "username", "photo uri", title, desc))

    mydb.commit()
