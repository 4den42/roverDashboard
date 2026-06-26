import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import StreamingResponse, FileResponse
from starlette.websockets import WebSocket, WebSocketDisconnect
from app.core.telemetry import telemetry_generator
from app.api.routes import router
import app.core.camera as camera_module
import asyncio

logger = logging.getLogger(__name__)

ALLOWED_ORIGINS = [
    "https://raspberrypi.taild8e577.ts.net",
    "http://localhost:8000",
    "http://100.78.160.76:8000",
]

app = FastAPI()

app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.websocket("/ws/telemetry")
async def telemetry_ws(websocket: WebSocket):
    origin = websocket.headers.get("origin")
    if origin is not None and origin not in ALLOWED_ORIGINS:
        logger.warning("Rejected WebSocket from origin: %r", origin)
        await websocket.close(code=1008)
        return
    await websocket.accept()
    try:
        async for data in telemetry_generator():
            await websocket.send_json(data)
    except WebSocketDisconnect:
        pass
    except Exception:
        logger.exception("WebSocket error in telemetry_ws")

async def generate():
    while True:
        if camera_module.latest_frame is None:
            await asyncio.sleep(0.03)
            continue
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + camera_module.latest_frame + b'\r\n')
        await asyncio.sleep(0.03)

@app.get("/camera")
async def camera_feed():
    return StreamingResponse(
        generate(),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )

app.mount("/assets", StaticFiles(directory="dist/assets"), name="assets")

@app.get("/{full_path:path}")
async def serve_frontend(full_path: str):
    return FileResponse("dist/index.html")
