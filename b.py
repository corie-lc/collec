import psycopg2

import psycopg2


def main():
    import mysql.connector

    mydb = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="681336",
        database="collec"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        print(x)


    insert_stmt = (

      "INSERT INTO users (name, username, email, password) "
      
      "VALUES (%s, %s, %s, %s)"
    )

    mydb.commit()
    data = ('corie leclair', 'corieleclair-dev', 'corieleclair.real@gmail.com', "681336")
    print(mycursor.rowcount, "record inserted.")
    mycursor.execute(insert_stmt, data)






if __name__ == "__main__":
    main()
