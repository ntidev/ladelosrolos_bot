# This file will create the Table and populate it with lines from the questions.txt file

import os
from pathlib import Path
from dotenv import load_dotenv
import mysql.connector
os.system('cls')

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Connects to the database
def connectToDB():
    connection = mysql.connector.connect(user=os.environ['DBUSERNAME'], password=os.environ['DBPASSWORD'],
                                        host=os.environ['DBHOST'],
                                        database=os.environ['DBNAME'])

    return connection


def createTable(connection,cursor):
    table_query = """CREATE TABLE questions (
	            id SERIAL PRIMARY KEY,
	            question VARCHAR(300) NOT NULL,
	            sent_status VARCHAR(5),
	            sent_on TIMESTAMP
                );"""

    cursor.execute(table_query)
    connection.commit()

connection = connectToDB()
cursor = connection.cursor()
# createTable(connection,cursor)

# Fill DB with questions from TXT file
with open(r"questions.txt",'r') as file:
    lines = file.read().splitlines()

    for line in lines:
        item = line.strip("\n")
        params = (item, )
        cursor.execute("INSERT INTO questions (question) VALUES (%s)", params)

connection.commit()
cursor.close()
connection.close()
print('Done adding elements to DB')