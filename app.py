import mysql
import mysql.connector
from sql_util.users import does_user_exist, crete_user, login, sql_update_user
from sql_util.posts import create_post, add_comment

from flask import Flask, render_template, redirect, request, session
from flask_session import Session


# init flask app, and secret key (used for security purposes)
app = Flask(__name__)
app.secret_key = '681336'


@app.route('/')
def hello_world():  # put application's code here
    # init session
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_TYPE"] = "filesystem"

    sess = Session()
    sess.init_app(app)

    Session(app)
    return render_template('Home.html')


@app.route('/post/<post_id>')
def post(post_id):
    # renders post.html page, renders page with correct post
    return render_template('post.html', para1=post_id)


@app.route('/settings')
def settings():
    return render_template('settings.html')


# creating user, sign up
@app.route('/signup', methods=['POST', 'GET'])
def signup():
    email = request.form['signup-email']
    name = request.form['signup-name']
    password = request.form['signup-password']

    if does_user_exist(email):
        return render_template("Home.html")
    else:
        crete_user(name, name, email, password)

    return render_template("Home.html")


@app.route('/login', methods=['POST', 'GET'])
def login_flask():
    # getting input from login page
    name = request.form.get("login-name")
    password = request.form.get("login-password")

    if login(name, password):
        # adding user to session
        session["username"] = name
        session["password"] = password
        return render_template("feed.html")
    else:
        return render_template("Home.html")


@app.route('/createpost', methods=['POST', 'GET'])
def create_post_flask():
    # collecting input from createpost
    title = request.form.get("title")
    desc = request.form.get("desc")
    name = request.form.get("photo-file")

    create_post(title, desc)

    return render_template("feed.html")


@app.route('/change_username', methods=['POST', 'GET'])
def change_username():
    username = request.form.get('new_username')
    old_password = request.form.get('old_password')

    if sql_update_user(session['username'], session['username'], username, old_password, 1):
        return render_template("Home.html")
    else:
        return render_template("settings.html")


@app.route('/change_email', methods=['POST', 'GET'])
def change_email():
    email = request.form.get('new_email')
    old_password = request.form.get('old_password')

    if sql_update_user(session['username'], session['email'], email, old_password, 2):
        return render_template("Home.html")
    else:
        return render_template("settings.html")


@app.route('/change_password', methods=['POST', 'GET'])
def change_password():
    new_password = request.form.get('new_password')
    old_password = request.form.get('old_password')
    print(new_password)
    print(old_password)

    if sql_update_user(session['username'], old_password, new_password, old_password, 3):
        return render_template("Home.html")
    else:
        return render_template("settings.html")

 # needs to be deleted
def test():
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
        posts.append(item)

    return posts


app.jinja_env.globals.update(test=test)

if __name__ == '__main__':
    app.run()
