import mysql.connector
try:

    connection = mysql.connector.connect(host='127.0.0.1',
                                         database='HW1_db',
                                         user='root',
                                         password='laila1369')
    # create_db_query = """CREATE DATABASE HW1_db"""
    #
    # create_table_query = """CREATE TABLE Employees (
    # id INT AUTO_INCREMENT PRIMARY KEY,
    # name VARCHAR(20),
    # weight int(3),
    # height int(3)
    # )"""
    # insert_data_query = """INSERT INTO Employees
    #  (name,weight,height)
    #  VALUES
    # (\'amin\',75,180),
    # (\'Mahdi\',90,190),
    # (\'Mohammad\',75,175),
    # (\'Ahmad\',60,175);"""
    select_data = """SELECT * FROM Employees order by height desc ,weight asc ;"""

    cursor = connection.cursor()
    # result = cursor.execute(create_db_query)
    # result = cursor.execute(create_table_query)
    # result2 = cursor.execute(insert_data_query)
    cursor.execute(select_data)
    myresult = cursor.fetchall()
    connection.commit()
    for _, name, weight, height in myresult:
        print(f'{name} {height} {weight}')

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
