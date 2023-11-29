from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

message = "Here i am trying to learn kafka"
producer.send('trackingGPS', message.encode('utf-8'))

producer.flush()
producer.close()