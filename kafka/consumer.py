from kafka import KafkaConsumer
import json
import config
import mysql.connector


def connect_database():
    user     = config.SQL_USER
    password = config.SQL_PASSWORD
    host     = config.SQL_HOST
    database = config.SQL_DATABASE
    auth     = config.SQL_AUTH
    port     = config.SQL_PORT
    # print("Connecting to database...")
    # print(f"User: {user}")
    # print(f"Password: {password}")
    # print(f"Host: {host}")
    # print(f"Database: {database}")
    # print(f"Auth: {auth}")
    # print(f"Port: {port}")
    cnx = mysql.connector.connect(
        host        = host,
        user        = user,
        password    = password,
        database    = database,
        auth_plugin = auth,
        port        = port
    )
    print("Done")
    return cnx


def create_table_in_BDD(cnx: mysql.connector.connect):
    print("Creating table in BDD...")
    cursor = cnx.cursor()
    # create table
    query = f"CREATE TABLE {config.SQL_TABLE} (id INT PRIMARY KEY, latitude FLOAT, longitude FLOAT)"
    print(query)
    cursor.execute(query)
    print("Done")
    return


def add_message_to_BDD(cnx: mysql.connector.connect, msg: dict):
    print("Adding message to BDD...")
    cursor = cnx.cursor()
    # add to BDD
    query = f"INSERT INTO {config.SQL_TABLE} (id, latitude, longitude) VALUES ({msg['id']}, {msg['lat']}, {msg['long']})"
    print(query)
    cursor.execute(query)
    cnx.commit()
    print("Done")
    return


def get_message_from_BDD(cnx: mysql.connector.connect):
    print("Getting message from BDD...")
    cursor = cnx.cursor()

    # read from BDD
    query = f"SELECT * FROM {config.SQL_TABLE}"
    print(query)
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
    print("Done")
    return


# Read messages from Kafka.
def read_messages():
    # Initiate BDD connection
    cnx = connect_database()

    # Get variables from config file
    topic = config.KAFKA_TOPIC
    bootstra_servers = config.KAFKA_SERVER_ADDRESS

    # Create a Kafka consumer
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=bootstra_servers,
        auto_offset_reset="earliest",
        group_id="consumer-group-a"
    )

    # Read messages from Kafka
    for message in consumer:
        # convert to json
        msg = json.loads(message.value)
        #TODO import func from package, or define func above ; and execute it as following :
        # func(msg) ; with msg = {"id":un id, "lat": une latitude, "long": une longitude}
        get_message_from_BDD(cnx)



if __name__ == "__main__":
    # cnx = connect_database()
    # msg = {"id":1, "lat": 1.0, "long": 1.0}
    # create_table_in_BDD(cnx)
    # add_message_to_BDD(cnx, msg)
    read_messages()