import json
from kafka import KafkaProducer
import random
import time
import config

def send_location(producer, user_id: str, lat: float, long: float):
    # Get variables from config file
    topic_name = config.KAFKA_TOPIC

    # Create a message
    message = {"ip_user": user_id, "lat": lat, "long": long}

    # Use the JSON serializer of the Kafka producer
    producer.send(topic_name, value=message)
    producer.flush()

    # Print message
    print(f"Produced message: {message}")

def generate_random_movement(current_lat: float, current_long: float):
    # Generate a small random movement to simulate realistic user movement
    delta_lat = random.uniform(-0.0001, 0.0001)
    delta_long = random.uniform(-0.0001, 0.0001)

    new_lat = current_lat + delta_lat
    new_long = current_long + delta_long

    return new_lat, new_long

if __name__ == "__main__":
    user_id = 192.168.1.45

    # Create a Kafka producer
    producer = KafkaProducer(
        bootstrap_servers=config.KAFKA_SERVER_ADDRESS,
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    try:
        while True:
            # Generate random initial coordinates
            lat = random.uniform(-90, 90).__round__(6)
            long = random.uniform(-180, 180).__round__(6)

            # Simulate realistic movement
            lat, long = generate_random_movement(lat, long)

            # Call the function to send the location
            send_location(producer, user_id, lat, long)

            # Sleep for x milliseconds before the next iteration
            time.sleep(500)  # Adjust the delay as needed

    finally:
        # Close the Kafka producer
        producer.close()
