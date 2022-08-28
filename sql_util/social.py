# social for collec

import mysql
import mysql.connector
from flask import session


def get_following(user):
    mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="681336",
        database="collec"
    )

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM social_conn")
    following = []

    for item in cursor:
        if item[0] == user and item[2] == "F":
            following.append(item[1])

    return following


def s_follow(user_followed):
    mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="681336",
        database="collec"
    )

    mycursor = mydb.cursor()

    mycursor.execute('''

                INSERT INTO social_conn
                VALUES (%s, %s, %s);

            ''', (session['username'], user_followed, "F"))

    mydb.commit()
