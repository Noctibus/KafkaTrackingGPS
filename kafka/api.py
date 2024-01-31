
import logging
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import asyncio
import json
from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
from aiohttp import web
from aiohttp.web import WebSocketResponse
from consumer import get_latest_message_from_BDD, initiate_database
import uvicorn



app = FastAPI(
    title="Tracking GPS",
    description="Simulation IoT d'un tracking GPS",
    version="0.1",
)
loop = asyncio.get_event_loop()


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
    initiate_database(host="database")
    return {"message": "Welcome on our API"}


fake_data = {
    "IP1": [
        {"latitude": 43.2953, "longitude": -0.3700},
        {"latitude": 43.2944, "longitude": -0.3705},
        {"latitude": 43.2981, "longitude": -0.3708},

        # Add more data points for IP1 as needed

    ],
    "IP2": [
        {"latitude": 40.7128, "longitude": -74.0060},
        {"latitude": 40.7129, "longitude": -74.005},
        {"latitude": 40.713, "longitude": -74.004},

        # Add more data points for IP2 as needed
    ],
}

@app.get("/fake-gps/{machine_id}")
async def get_fake_gps(machine_id: str):
    msg = get_latest_message_from_BDD(ip=machine_id, host="database")
    return msg


if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000)