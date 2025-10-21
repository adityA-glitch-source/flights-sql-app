import mysql.connector
import os

class DB:
    def __init__(self):
        # Connect to the Database

        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user=os.getenv('MY_USERNAME'),
                password=os.getenv('MY_PASSWORD'),
                database='indigo'
            )
            self.cursor = self.conn.cursor()
            print('Connected to MySQL database')
        except mysql.connector.Error as err:
            print(err)
    def fetch_city_names(self):
        city = []
        self.cursor.execute(""" SELECT DISTINCT Destination From `flights_cleaned - flights_cleaned`
                                UNION 
                                SELECT DISTINCT Source From `flights_cleaned - flights_cleaned`
                                
                            

                               """)
        data = self.cursor.fetchall()

        for item in data:
            city.append(item[0])
        return city