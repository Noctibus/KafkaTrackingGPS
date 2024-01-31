import json
from kafka import KafkaProducer
import random
import config
import sys


# Send message to Kafka.
def send_location(user:int, lat:float, long:float):
    # Get variables from config filr
    topic_name = config.KAFKA_TOPIC
    bootstrap_servers = config.KAFKA_SERVER_ADDRESS

    # Create a Kafka producer
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

    # Create a message
    message = {"user":user, "lat": lat, "long": long}
    message_json = json.dumps(message).encode("utf-8")

    # Send the message
    producer.send(topic_name, message_json)
    producer.flush()

    # Print message
    print(f"Produced message: {message}")


if __name__ == "__main__":

    user = sys.argv[1]
    # random lat/long for example
    lat = random.uniform(-90, 90).__round__(6)
    long = random.uniform(-180, 180).__round__(6)

    # Call the function to send the location
    send_location(user, lat, long)