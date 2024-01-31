from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import asyncio

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
    allow_methods=["*"],  
    allow_headers=["*"],  
)

@app.get("/")
async def index():
    return {"message": "Welcome on our API"}

fake_data = [
    {"latitude": 43.2953, "longitude": -0.3700},
    {"latitude": 43.2944, "longitude": -0.3705},
    {"latitude": 43.2981, "longitude": -0.3708},
    {"latitude": 40.7128, "longitude": -74.0060},
    {"latitude": 40.7129, "longitude": -74.005},
    {"latitude": 40.713, "longitude": -74.004},
]

@app.get("/test")
async def get_fake_gps():
    return fake_data

@app.get("/ws")
async def get_fake_gps():
    return fake_data

