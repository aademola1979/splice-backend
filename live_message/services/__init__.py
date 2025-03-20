from fastapi import WebSocket, WebSocketDisconnect
from typing import List
import json


class SocketConnectionManager:
    def __init__(self):
        self.active_connection: List[WebSocket] = []

    async def connect(self, websocket:WebSocket):
        await websocket.accept()
        self.active_connection.append(websocket)

    def disconnect(self, websocket:WebSocket):
        self.active_connection.remove(websocket)

    async def broadcast(self, message:str):
        for connection in self.active_connection:
            await connection.send(message)


manager = SocketConnectionManager()

async def chat_endpoint(websocket:WebSocket):
    await manager.connect(websocket=websocket)
    try:
        while True:
            data = await websocket.receive_text()
            message_data = json.loads(data)
            formatted_message = f'[{message_data['username']}] {message_data['message']}'
            await manager.broadcast(f'client says: {formatted_message}')
    except WebSocketDisconnect:
        manager.disconnect(websocket=websocket)
        await manager.broadcast('A client has ledt the chat!')

