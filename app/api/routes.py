from fastapi import APIRouter
from app.hardware.motors import handle_command

router = APIRouter()

@router.post("/api/control")
async def control(data: dict):
    command = data.get("command")

    print("COMMAND RECEIVED:", command)

    handle_command(command)

    return {"status": "ok", "command": command}
