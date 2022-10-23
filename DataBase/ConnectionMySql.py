import mysql.connector
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='student',
                                         user='root',
                                         password='kingraju12345.')
    if connection.is_connected():
        print("Connected to DataBase")
    else:
        print("Failed")
except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
