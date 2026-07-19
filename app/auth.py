import os
import secrets
from fastapi import APIRouter, Cookie, HTTPException, Request, Response

SESSION_TOKENS: set[str] = set()
_PASSWORD = os.environ.get("ROVER_PASSWORD", "")

auth_router = APIRouter()


def require_auth(session: str | None = Cookie(default=None)) -> None:
    if not session or session not in SESSION_TOKENS:
        raise HTTPException(status_code=401, detail="Not authenticated")


@auth_router.post("/api/login")
async def login(request: Request, response: Response):
    if not _PASSWORD:
        raise HTTPException(status_code=500, detail="ROVER_PASSWORD env var not set")
    body = await request.json()
    if not secrets.compare_digest(body.get("password", ""), _PASSWORD):
        raise HTTPException(status_code=401, detail="Wrong password")
    token = secrets.token_urlsafe(32)
    SESSION_TOKENS.add(token)
    response.set_cookie("session", token, httponly=True, samesite="strict")
    return {"status": "ok"}


@auth_router.post("/api/logout")
async def logout(response: Response, session: str | None = Cookie(default=None)):
    if session:
        SESSION_TOKENS.discard(session)
    response.delete_cookie("session")
    return {"status": "ok"}


@auth_router.get("/api/auth/check")
async def auth_check(session: str | None = Cookie(default=None)):
    if not session or session not in SESSION_TOKENS:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return {"status": "ok"}
