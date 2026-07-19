from typing import Literal
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.auth import require_auth
from app.hardware.motors import handle_command
from app.hardware.lights import set_light, get_light

router = APIRouter(dependencies=[Depends(require_auth)])

class ControlRequest(BaseModel):
    command: Literal["forward", "backward", "left", "right", "stop"]

class LightRequest(BaseModel):
    state: bool

@router.post("/api/control")
async def control(data: ControlRequest):
    handle_command(data.command)
    return {"status": "ok", "command": data.command}

@router.post("/api/light")
async def light(data: LightRequest):
    set_light(data.state)
    return {"status": "ok", "state": data.state}

@router.get("/api/light")
async def light_state():
    return {"state": get_light()}
