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
    def fetch_all_flights(self,source,destination):
        self.cursor.execute(""" 
                            SELECT Airline,Route,Dep_Time,Duration 
                            FROM `flights_cleaned - flights_cleaned`
                            Where Source = '{}' 
                            AND Destination = '{}' 
                            """.format(source,destination))
        data = self.cursor.fetchall()
        return data
    def fetch_airline_frequency(self):
        airline = []
        frequency = []
        self.cursor.execute(""" 
        SELECT Airline,COUNT(*)
        FROM `flights_cleaned - flights_cleaned`
        GROUP BY Airline
        """)
        data = self.cursor.fetchall()
        for item in data:
            airline.append(item[0])
            frequency.append(item[1])
        return airline, frequency
    def busy_airport(self):
        city = []
        frequency = []

        self.cursor.execute("""
                SELECT Source,COUNT(*) FROM (SELECT Source FROM `flights_cleaned - flights_cleaned`
        							UNION ALL
        							SELECT Destination FROM `flights_cleaned - flights_cleaned`) t
                GROUP BY t.Source
                ORDER BY COUNT(*) DESC
                """)

        data = self.cursor.fetchall()

        for item in data:
            city.append(item[0])
            frequency.append(item[1])

        return city, frequency

    def daily_frequency(self):
        date = []
        frequency = []

        self.cursor.execute("""
                SELECT Date_of_Journey,COUNT(*) FROM `flights_cleaned - flights_cleaned`
                GROUP BY Date_of_Journey
                """)

        data = self.cursor.fetchall()

        for item in data:
            date.append(item[0])
            frequency.append(item[1])

        return date, frequency