import re

import mysql.connector


def create_db():
    try:

        connection = mysql.connector.connect(host='127.0.0.1',
                                             user='root',
                                             database='HW2_db',
                                             password='laila1369')
        # create_db_query = """CREATE DATABASE HW2_db"""

        create_table_query = """CREATE TABLE Users (id INT AUTO_INCREMENT PRIMARY KEY,username VARCHAR(20),password varchar(20));"""

        cursor = connection.cursor()
        # result = cursor.execute(create_db_query)
        result = cursor.execute(create_table_query)
        connection.commit()

    except mysql.connector.Error as error:
        print("Failed to create table in MySQL: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def main():
    username = ''
    while not username:
        username = input()
        password = input()
        email_pattern = "\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*"
        if not re.match(email_pattern, username) :
            print('Invalid email format,correct format is "laila@gmail.com"')
            username = ''

    try:
        connection = mysql.connector.connect(host='127.0.0.1',
                                             database='HW2_db',
                                             user='root',
                                             password='laila1369')

        insert_data_query = "INSERT INTO Users (username,password) VALUES (%s,%s);"
        values = (username, password)
        cursor = connection.cursor()
        result = cursor.execute(insert_data_query, values)
        connection.commit()



    except mysql.connector.Error as error:

        connection.rollback()

        print("Failed to insert into MySQL table {}".format(error))


    finally:

        if connection.is_connected():
            cursor.close()

            connection.close()

            print("MySQL connection is closed")


# create_db()
main()
