from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from app.core.telemetry import telemetry_generator

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.websocket("/ws/telemetry")
async def telemetry_ws(websocket: WebSocket):
    await websocket.accept()

    async for data in telemetry_generator():
        await websocket.send_json(data)
