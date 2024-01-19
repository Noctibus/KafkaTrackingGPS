from kafka import KafkaConsumer
import json
import config


# Read messages from Kafka.
def read_messages():
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

if __name__ == "__main__":
    read_messages()