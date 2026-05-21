from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from app.core.telemetry import telemetry_generator
from fastapi.responses import StreamingResponse
import app.core.camera as camera_module
import asyncio

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

async def generate():
    while True:
        if camera_module.latest_frame is None:
            await asyncio.sleep(0.03)
            continue
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + camera_module.latest_frame + b'\r\n')
        await asyncio.sleep(0.03)

@app.get("/camera")
def camera_feed():
    return StreamingResponse(
        generate(),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )
