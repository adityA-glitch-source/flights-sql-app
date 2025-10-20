import mysql.connector
import os

class DB:
    def __init__(self):
        # Connect to the Database

        try:
            conn = mysql.connector.connect(
                host='localhost',
                user=os.getenv('MY_USERNAME'),
                password=os.getenv('MY_PASSWORD'),
                database='indigo'
            )
            cursor = conn.cursor()
            print('Connected to MySQL database')
        except mysql.connector.Error as err:
            print(err)