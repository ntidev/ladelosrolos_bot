# SlackBot that sends watercooler questions to a Slack Channel. Questions are coming from a DB with multiple columns: Questions, Sent Status, Timestamp

import mysql.connector
import os
import slack
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path



env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])

# Connection to the database
# Database contains: Index, Question, Sent Status. Status can be Yes or Null/empty
def dbConnection():
    connection = mysql.connector.connect(user=os.environ['DBUSERNAME'],
                                        password=os.environ['DBPASSWORD'],
                                        host=os.environ['DBHOST'],
                                        database=os.environ['DBNAME'])

    return connection


# Function that will go into the DB and bring one random question. Script will proceed if sent_status is none
def pickSendQuestion(connection, cursor):

    sent = 'Sent'
    pick_record = "SELECT * FROM questions ORDER BY RAND() LIMIT 1"

    while sent == 'Sent':
        cursor.execute(pick_record)
        record = cursor.fetchone()

        if record[2] == None:
            print(record[1])
            postMessage(record[1])
            updateRecord(connection, record)
            sent = 'None'


# Function that takes care of posting the message in the specified Slack Channel
def postMessage(question):
    client.chat_postMessage(channel=os.environ['SLACK_CHANNEL'], text="HOLAAA VECINOS Y VECINAS!!! UNA PREGUNTICA!!\n\n" + question)
    print('Question sent to Slack.\n')
    

# Function that updates the row that was previously sent via Slack. The purpose is to mark it as Sent 
def updateRecord(connection, record):
    
    update_record = "UPDATE questions set sent_status = 'Sent', sent_on = %s  WHERE id = %s"
    id = record[0]
    time = datetime.now()
    params = (time, id, )
    cursor.execute(update_record,params)
    connection.commit()
    print('Status and Timestamp changed\n')


# Connect to DB
connection = dbConnection()
cursor = connection.cursor()

# Pick & Send Question
pickSendQuestion(connection,cursor)

# Close connection
cursor.close()
connection.close()
