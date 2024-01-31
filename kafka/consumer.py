from kafka import KafkaConsumer
import json
import config
import mysql.connector
from pprint import pprint
from datetime import datetime


def connect_database(host:str=config.SQL_HOST):
    user     = config.SQL_USER
    password = config.SQL_PASSWORD
    database = config.SQL_DATABASE
    auth     = config.SQL_AUTH
    port     = config.SQL_PORT
    cnx = mysql.connector.connect(
        host        = host,
        user        = user,
        password    = password,
        database    = database,
        auth_plugin = auth,
        port        = port
    )
    return cnx


def create_table_in_BDD(cnx: mysql.connector.connect):
    cursor = cnx.cursor()
    # create table
    query = f"CREATE TABLE {config.SQL_TABLE} (id INT PRIMARY KEY, latitude FLOAT, longitude FLOAT)"
    cursor.execute(query)
    return


def add_message_to_BDD(cnx: mysql.connector.connect, msg: dict):
    cursor = cnx.cursor()
    # add to BDD
    query = f"INSERT INTO {config.SQL_TABLE} (user, latitude, longitude) VALUES ({msg['user']}, {msg['lat']}, {msg['long']})"
    cursor.execute(query)
    cnx.commit()
    return


def get_message_from_BDD(id:int, cnx: mysql.connector.connect=None, host:str=config.SQL_HOST, time:datetime=None):
    if cnx is None:
        cnx = connect_database(host)
    cursor = cnx.cursor()

    # read from BDD
    query = f"SELECT * FROM {config.SQL_TABLE} where id={id}"
    cursor.execute(query)
    result = cursor.fetchall()
    return result


def get_latest_message_from_BDD(id:int, cnx: mysql.connector.connect=None, host:str=config.SQL_HOST, time:datetime=None):
    if cnx is None:
        cnx = connect_database(host)
    cursor = cnx.cursor()

    # read from BDD
    query = f"SELECT * FROM {config.SQL_TABLE} where id={id} ORDER BY id DESC LIMIT 1"
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def kafka_consumer(bootstrap_servers:str = config.KAFKA_SERVER_ADDRESS):
    # Get variables from config file
    topic = config.KAFKA_TOPIC
    bootstra_servers = config.KAFKA_SERVER_ADDRESS

    # Create a Kafka consumer
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=bootstra_servers,
        auto_offset_reset="earliest",
        group_id="consumer-1"
    )

    return consumer



# Read messages from Kafka.
def read_messages():
    # Initiate BDD connection
    cnx = connect_database()

    consumer = kafka_consumer("kafka:9092")

    # Read messages from Kafka
    for message in consumer:
        # convert to json
        msg = json.loads(message.value)
        add_message_to_BDD(cnx, msg)



if __name__ == "__main__":
    # cnx = connect_database()
    # msg = {"id":1, "lat": 1.0, "long": 1.0}
    # create_table_in_BDD(cnx)
    # add_message_to_BDD(cnx, msg)
    read_messages()