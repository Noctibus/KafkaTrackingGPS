import json
from kafka import KafkaProducer
import random
import config


# Send message to Kafka.
def send_location(id:int, lat:float, long:float):
    # Get variables from config filr
    topic_name = config.KAFKA_TOPIC
    bootstrap_servers = config.KAFKA_SERVER_ADDRESS

    # Create a Kafka producer
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

    # Create a message
    message = {"id":id, "lat": lat, "long": long}
    message_json = json.dumps(message).encode("utf-8")

    # Send the message
    producer.send(topic_name, message_json)
    producer.flush()

    # Print message
    print(f"Produced message: {message}")


if __name__ == "__main__":

    id = 0
    # random lat/long for example
    lat = random.uniform(-90, 90).__round__(6)
    long = random.uniform(-180, 180).__round__(6)

    # Call the function to send the location
    send_location(id, lat, long)