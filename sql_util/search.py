import mysql
import mysql.connector
from flask import session

from sql_util.social import get_following


def get_relevant_posts():
    mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="681336",
        database="collec"
    )

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM userposts")
    posts = []
    relevant_posts = []

    for item in cursor:
        posts.append(item)

    for item in posts:
        for following in get_following(session['username']):
            if item[1] == following:
                relevant_posts.append(item)

    relevant_posts.extend(posts)

    print(posts)
    return relevant_posts


def search_sql(search_entry):
    print(search_entry)
    mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="681336",
        database="collec"
    )

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM userposts")
    posts = []

    for item in cursor:
        if len(str(search_entry)) > 0:
            print(search_entry)
            if str(search_entry) in item[3]:
                posts.append(item)
            else:
                pass
        else:
            posts.append(item)

    print(posts)
    return posts