import mysql.connector
import os
from mysql.connector import Error
#connect to the database server
try:
    conn = mysql.connector.connect(
           host='localhost',
           user=os.getenv('MY_USERNAME'),
           password = os.getenv('MY_PASSWORD')
    )
    cursor = conn.cursor()
    print('Connected to MySQL database')
except mysql.connector.Error as err:
    print(err)
#CREATE A DATABASE ON THE DB SERVER
cursor.execute('CREATE DATABASE indigo')
conn.commit()