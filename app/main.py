import logging
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import StreamingResponse, FileResponse
from starlette.websockets import WebSocket, WebSocketDisconnect
from app.core.telemetry import telemetry_generator
from app.api.routes import router
from app.auth import auth_router, check_session, require_auth
import app.core.camera as camera_module
import asyncio

logger = logging.getLogger(__name__)

connected_clients = 0
_clients_lock = asyncio.Lock()

ALLOWED_ORIGINS = [
    "https://raspberrypi.taild8e577.ts.net",
    "http://localhost:8000",
]

app = FastAPI()

app.include_router(auth_router)
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
    global connected_clients
    if not check_session(websocket.cookies.get("session")):
        await websocket.close(code=1008)
        return
    origin = websocket.headers.get("origin")
    if origin is not None and origin not in ALLOWED_ORIGINS:
        logger.warning("Rejected WebSocket from origin: %r", origin)
        await websocket.close(code=1008)
        return
    await websocket.accept()
    async with _clients_lock:
        connected_clients += 1
        if connected_clients == 1:
            camera_module.capture_active.set()
            logger.info("Client connected — camera active")
    try:
        async for data in telemetry_generator():
            await websocket.send_json(data)
    except WebSocketDisconnect:
        pass
    except Exception:
        logger.exception("WebSocket error in telemetry_ws")
    finally:
        async with _clients_lock:
            connected_clients -= 1
            if connected_clients == 0:
                camera_module.capture_active.clear()
                logger.info("No clients — camera paused")

@app.get("/camera", dependencies=[Depends(require_auth)])
async def camera_feed():
    async def stream():
        global connected_clients
        async with _clients_lock:
            connected_clients += 1
            if connected_clients == 1:
                camera_module.capture_active.set()
                logger.info("Camera client connected — camera active")
        try:
            while True:
                if camera_module.latest_frame is None:
                    await asyncio.sleep(0.03)
                    continue
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + camera_module.latest_frame + b'\r\n')
                await asyncio.sleep(0.03)
        finally:
            async with _clients_lock:
                connected_clients -= 1
                if connected_clients == 0:
                    camera_module.capture_active.clear()
                    logger.info("No clients — camera paused")

    return StreamingResponse(stream(), media_type="multipart/x-mixed-replace; boundary=frame")

app.mount("/assets", StaticFiles(directory="dist/assets"), name="assets")

@app.get("/{full_path:path}")
async def serve_frontend(full_path: str):
    return FileResponse("dist/index.html")
