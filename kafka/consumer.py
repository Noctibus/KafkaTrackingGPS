from kafka import KafkaConsumer
import json
import config
import mysql.connector
from datetime import datetime


def connect_database(host:str=config.SQL_HOST, database=config.SQL_DATABASE):
    user     = config.SQL_USER
    password = config.SQL_PASSWORD
    database = config.SQL_DATABASE
    auth     = config.SQL_AUTH
    port     = config.SQL_PORT
    if database is not None:
        cnx = mysql.connector.connect(
            host        = host,
            user        = user,
            password    = password,
            database    = database,
            auth_plugin = auth,
            port        = port
    )
    else:
        cnx = mysql.connector.connect(
            host        = host,
            user        = user,
            password    = password,
            auth_plugin = auth,
            port        = port
        )
    return cnx


def initiate_database(cnx: mysql.connector.connect=None, host:str=config.SQL_HOST):
    if cnx is None:
        cnx = connect_database(host, database=None)
    cursor = cnx.cursor()
    # create table
    query = f"CREATE DATABASE IF NOT EXISTS {config.SQL_DATABASE}"
    cursor.execute(query)
    query = "CREATE TABLE IF NOT EXISTS history (id INT AUTO_INCREMENT, latitude DOUBLE NOT NULL, longitude DOUBLE NOT NULL, user_ip VARCHAR(50) NOT NULL, PRIMARY KEY (id));"
    cursor.execute(query)
    return


def add_message_to_BDD(cnx: mysql.connector.connect, msg: dict):
    cursor = cnx.cursor()
    # add to BDD
    query = f"INSERT INTO {config.SQL_TABLE} (user_ip, latitude, longitude) VALUES ('{msg['user_ip']}', {msg['latitude']}, {msg['longitude']})"
    cursor.execute(query)
    cnx.commit()
    return


def get_message_from_BDD(ip:str, cnx: mysql.connector.connect=None, host:str=config.SQL_HOST, time:datetime=None):
    if cnx is None:
        cnx = connect_database(host)
    cursor = cnx.cursor()

    # read from BDD
    query = f"SELECT * FROM {config.SQL_TABLE} where user_ip={ip}"
    cursor.execute(query)
    result = cursor.fetchall()
    return result


def get_latest_message_from_BDD(ip:str, cnx: mysql.connector.connect=None, host:str=config.SQL_HOST, time:datetime=None):
    if cnx is None:
        cnx = connect_database(host)
    cursor = cnx.cursor()

    # read from BDD
    query = f"SELECT * FROM {config.SQL_TABLE} where user_ip='{ip}' ORDER BY id DESC LIMIT 1"
    cursor.execute(query)
    result = cursor.fetchall()[0]
    return result

def kafka_consumer(bootstrap_servers:str = config.KAFKA_SERVER_ADDRESS):
    # Get variables from config file
    topic = config.KAFKA_TOPIC
    bootstrap_servers = config.KAFKA_SERVER_ADDRESS

    # Create a Kafka consumer
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=bootstrap_servers,
        auto_offset_reset="earliest",
        group_id="consumer-1"
    )

    return consumer



# Read messages from Kafka.
def read_messages(host:str=config.SQL_HOST, bootstrap_servers:str=config.KAFKA_SERVER_ADDRESS):
    # Initiate BDD connection
    cnx = connect_database(host=host)

    consumer = kafka_consumer(bootstrap_servers=bootstrap_servers)

    # Read messages from Kafka
    for message in consumer:
        # convert to json
        msg = json.loads(message.value)
        print(msg)
        add_message_to_BDD(cnx, msg)



if __name__ == "__main__":
    # read_messages(host="database", bootstrap_servers="kafka:9092")
    read_messages(host="localhost")