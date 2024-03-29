from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, WebSocket
import asyncio
from consumer import get_latest_message_from_BDD
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
    {"latitude": 43.3000, "longitude": -0.366667},
]

@app.get("/test")
async def get_fake_gps():
    return fake_data

active_connections = {}

@app.get("/ws")
async def websocket_endpoint(websocket: WebSocket, machine_id: str):
    await websocket.accept()

    try:
        while True:
            await asyncio.sleep(1)
            data = get_latest_message_from_BDD(ip=machine_id, host="database")
            # for gps_data in fake_data:
            await websocket.send_json(data)
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        await websocket.close()


if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000)