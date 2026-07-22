import os
import secrets
import time
from collections import defaultdict
from fastapi import APIRouter, Cookie, HTTPException, Request, Response

SESSION_TOKENS: dict[str, float] = {}  # token → expiry timestamp
_PASSWORD = os.environ.get("ROVER_PASSWORD", "")
_SESSION_TTL = 24 * 3600   # 24 hours
_RATE_WINDOW = 60           # seconds
_RATE_MAX = 10              # max failed attempts per window per IP

auth_router = APIRouter()
_failed_attempts: dict[str, list[float]] = defaultdict(list)


def check_session(token: str | None) -> bool:
    if not token or token not in SESSION_TOKENS:
        return False
    if time.time() > SESSION_TOKENS[token]:
        SESSION_TOKENS.pop(token, None)
        return False
    return True


def require_auth(session: str | None = Cookie(default=None)) -> None:
    if not check_session(session):
        raise HTTPException(status_code=401, detail="Not authenticated")


@auth_router.post("/api/login")
async def login(request: Request, response: Response):
    if not _PASSWORD:
        raise HTTPException(status_code=500, detail="ROVER_PASSWORD env var not set")

    ip = request.client.host
    now = time.time()
    _failed_attempts[ip] = [t for t in _failed_attempts[ip] if now - t < _RATE_WINDOW]
    if len(_failed_attempts[ip]) >= _RATE_MAX:
        raise HTTPException(status_code=429, detail="Too many login attempts")

    body = await request.json()
    if not secrets.compare_digest(body.get("password", ""), _PASSWORD):
        _failed_attempts[ip].append(now)
        raise HTTPException(status_code=401, detail="Wrong password")

    _failed_attempts.pop(ip, None)
    expired = [t for t, exp in SESSION_TOKENS.items() if exp < now]
    for t in expired:
        SESSION_TOKENS.pop(t, None)

    token = secrets.token_urlsafe(32)
    SESSION_TOKENS[token] = now + _SESSION_TTL
    response.set_cookie("session", token, httponly=True, samesite="strict", secure=True)
    return {"status": "ok"}


@auth_router.post("/api/logout")
async def logout(response: Response, session: str | None = Cookie(default=None)):
    if session:
        SESSION_TOKENS.pop(session, None)
    response.delete_cookie("session", httponly=True, samesite="strict", secure=True)
    return {"status": "ok"}


@auth_router.get("/api/auth/check")
async def auth_check(session: str | None = Cookie(default=None)):
    if not check_session(session):
        raise HTTPException(status_code=401, detail="Not authenticated")
    return {"status": "ok"}
