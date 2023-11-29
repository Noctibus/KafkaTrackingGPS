from kafka import KafkaConsumer

topic = 'trackingGPS'

consumer = KafkaConsumer(topic, bootstrap_servers=['localhost:9092'], auto_offset_reset='earliest')

print('Starting the consumer')
for message in consumer:
    print(message)
