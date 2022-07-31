import mysql
import mysql.connector


def login(name, password):
    # init server
    mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="681336",
        database="collec"
    )

    # cursor is controller for server
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users")

    for user in cursor:
        if user[1] == name and user[3] == password:
            return True

    return False


def crete_user(name, username, email, password):
    mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="681336",
        database="collec"
    )

    mycursor = mydb.cursor()

    mycursor.execute('''
        
        INSERT INTO users
        VALUES (%s, %s, %s, %s);
    
    ''', (name, username, email, password))

    mydb.commit()


def does_user_exist(user_email):
    mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="681336",
        database="collec"
    )

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM users")

    for user in cursor:
        print(user[2])
        print(user_email)
        if user[2] == user_email:
            print('exits')
            return True

    return False


def sql_update_user(username, old, new, password, update_type):
    mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="681336",
        database="collec"
    )

    cursor = mydb.cursor(buffered=True)
    cursor.execute("SELECT * FROM users")

    for user in cursor:
        if user[1] == username and password == user[3]:
            print("here")

            # username
            if update_type == 1:

                sql = """
                   UPDATE users
                   SET username=%s
                   where username=%s
                """

                var = (new, old)

                cursor.execute(sql, var)

                mydb.commit()

                return True

            # email
            elif update_type == 2:
                sql = """
                        UPDATE users
                        SET email=%s
                        where email=%s
                    """

                var = (new, old)

                cursor.execute(sql, var)

                mydb.commit()
                return True

            elif update_type == 3:
                print("HEREe")
                sql = """
                        UPDATE users
                        SET password=%s
                        where password=%s
                    """

                var = (new, password)

                cursor.execute(sql, var)

                mydb.commit()
                return True

        else:
            print("verification failure")





# does_user_exist("dev")
