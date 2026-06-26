from fastapi import APIRouter
from app.hardware.motors import handle_command
from app.hardware.lights import set_light, get_light

router = APIRouter()

@router.post("/api/control")
async def control(data: dict):
    command = data.get("command")
    print("COMMAND RECEIVED:", command)
    handle_command(command)
    return {"status": "ok", "command": command}

@router.post("/api/light")
async def light(data: dict):
    state = bool(data.get("state", False))
    set_light(state)
    return {"status": "ok", "state": state}

@router.get("/api/light")
async def light_state():
    return {"state": get_light()}
