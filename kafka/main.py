from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import uvicorn
from consumer import kafka_consumer, get_latest_message_from_BDD
from pprint import pprint
import json
from datetime import datetime


app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    # consumer = kafka_consumer("kafka:9092")

    while True:
        id = await websocket.receive_text()
        msg = get_latest_message_from_BDD(int(id), host="database")
        websocket.send_text(f"Message text was: {msg}")



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)