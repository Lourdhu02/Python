from dbm.dumb import _Database
from multiprocessing.connection import _ConnectionBase, Connection
from sqlite3 import Cursor
import mysql.connector
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='student',
                                         user='root',
                                         password='kingraju12345.')

    mySql_Create_Table_Query = """CREATE TABLE Laptop ( 
                             Id int(11) NOT NULL,
                             Name varchar(250) NOT NULL,
                             Price float NOT NULL,
                             Purchase_date Date NOT NULL,
                             PRIMARY KEY (Id)) """

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Laptop Table created successfully ")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
