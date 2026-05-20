from fastapi import FastAPI, WebSocket
from app.api.routes import router
from app.core.telemetry import telemetry_generator

app = FastAPI()

app.include_router(router)

# WebSocket for live telemetry
@app.websocket("/ws/telemetry")
async def telemetry_ws(websocket: WebSocket):
    await websocket.accept()

    async for data in telemetry_generator():
        await websocket.send_json(data)
