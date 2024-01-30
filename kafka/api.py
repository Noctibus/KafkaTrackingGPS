from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from aiokafka import AIOKafkaConsumer, AIOKafkaProducer

app = FastAPI(
    title="Tracking GPS",
    description="Simulation IoT d'un tracking GPS",
    version="0.1",
)


origins = [
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # You might want to restrict this to specific HTTP methods
    allow_headers=["*"],  # You might want to restrict this to specific headers
)

@app.get("/")
async def index():
    return {"message": "Welcome on our API"}

# async def data_gps(data: dict):
#     """Some (fake) gps coordinates data."""
#     await asyncio.sleep(2)
#     message_processed = data.get("message", "").upper()
#     return message_processed

# # Replace 'your_kafka_bootstrap_servers' with your actual Kafka bootstrap servers
# KAFKA_BOOTSTRAP_SERVERS = 'your_kafka_bootstrap_servers'
# KAFKA_TOPIC = 'gps_data_topic'

# # Create a Kafka consumer
# consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS, group_id='gps_consumer')

# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     # Accept the connection from a client.
#     await websocket.accept()
#     while True:
#         try:
#             # Receive the PostgreSQL data sent by a client.
#             data = await websocket.receive_json()
#             # Some (fake) heavey data processing logic.
#             message_processed = await data_gps(data)
#             # Send JSON data to the client.
#             await websocket.send_json(
#                 {
#                     "message": message_processed,
#                     "time": datetime.now().strftime("%H:%M:%S"),
#                 }
#             )
#         except WebSocketDisconnect:
#             logger.info("The connection is closed.")
#             break

fake_data = {
    "IP1": [
        {"latitude": 43.2953, "longitude": -0.3700},
        {"latitude": 43.2944, "longitude": -0.3705},
        {"latitude": 43.2981, "longitude": -0.3708},
    ],
    "IP2": [
        {"latitude": 40.7128, "longitude": -74.0060},
        {"latitude": 40.7129, "longitude": -74.005},
        {"latitude": 40.713, "longitude": -74.004},
    ],
}

@app.get("/fake-gps/{machine_id}")
async def get_fake_gps(machine_id: str):
    if machine_id not in fake_data:
        return {"error": "Machine not found"}

    return fake_data[machine_id]
