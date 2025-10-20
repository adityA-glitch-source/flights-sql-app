import mysql.connector
import os
from mysql.connector import Error
#connect to the database server
try:
    conn = mysql.connector.connect(
           host='localhost',
           user=os.getenv('MY_USERNAME'),
           password = os.getenv('MY_PASSWORD'),
           database='indigo'
    )
    cursor = conn.cursor()
    print('Connected to MySQL database')
except mysql.connector.Error as err:
    print(err)
#CREATE A DATABASE ON THE DB SERVER
#cursor.execute('CREATE DATABASE indigo')
#conn.commit()

#Create a Table
cursor.execute('''
               CREATE TABLE IF NOT EXISTS airport (
                airport_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                code VARCHAR(10) NOT NULL,
                city VARCHAR(50) NOT NULL,
                name VARCHAR(255)
                )
               
               ''')
conn.commit()

#Insert data to the table
#cursor.execute('''
            #  INSERT INTO airport (code,city,name)
             # VALUES
              # ('DEL', 'NEW DELHI', 'IGIA'),
              # ('CCU', 'kolkata', 'NSCA'),
              # ('BOM', 'Mumbai', 'CSMA')
              
             # ''')
#conn.commit()

#search/retrieve
cursor.execute('select * from airport WHERE airport_id > 1')
data = cursor.fetchall()
for row in data:
    print(row[3])

# Update
cursor.execute("""
               UPDATE airport
               SET name = 'Bombay'
               WHERE airport_id = 3
               """)
conn.commit()

cursor.execute('select * from airport')
data = cursor.fetchall()
print(data)

#Delete
cursor.execute("Delete from airport WHERE airport_id = 3  ")
conn.commit()

cursor.execute("select * from airport")

data = cursor.fetchall()

