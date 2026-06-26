# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project is

A real-time rover telemetry and control dashboard. The frontend is Vue 3 + Vite + TypeScript; the backend is FastAPI running on a Raspberry Pi. In production, the FastAPI server serves the built frontend as static files, so there is one origin for both the API and the UI.

## Commands

### Frontend
```sh
npm install          # install dependencies
npm run dev          # Vite dev server (frontend only, no Python backend)
npm run build        # type-check + build to dist/
npm run lint         # oxlint + eslint (both with --fix)
npm run format       # prettier over src/
npm run test:unit    # vitest
npm run test:e2e     # playwright (requires a build first)
```

### Backend
```sh
# Activate the venv first
source venv/bin/activate

# Run directly
uvicorn app.main:app --host 0.0.0.0 --port 8000

# Restart the systemd service (pre-approved permission)
sudo systemctl restart roverdash
```

### Deployment
After changing the frontend, rebuild and restart:
```sh
npm run build && sudo systemctl restart roverdash
```
The FastAPI server picks up `dist/` directly — no separate deploy step.

## Architecture

```
roverDashboard/
├── app/                   # FastAPI backend
│   ├── main.py            # App entry point; mounts router, CORS, WebSocket, camera stream, serves dist/
│   ├── api/routes.py      # POST /api/control → motors.handle_command()
│   ├── core/
│   │   ├── telemetry.py   # Async generator: CPU/RAM/temp/wifi/uptime, yields every 1 s
│   │   └── camera.py      # cv2 capture loop in a daemon thread; latest_frame shared globally
│   └── hardware/
│       └── motors.py      # Stub: maps command strings to GPIO actions (currently just prints)
├── src/                   # Vue 3 frontend source
│   ├── views/dashBoardView.vue   # Single page: TelemetryPanel + CameraFeed + ControlPad
│   ├── components/
│   │   ├── telemetryPanel.vue    # Reads from telemetry Pinia store
│   │   ├── cameraFeed.vue        # <img> pointing at /camera (MJPEG stream)
│   │   └── controlPad.vue        # D-pad buttons → POST /api/control
│   ├── composables/useWebSocket.js  # Singleton WS to /ws/telemetry; auto-reconnects every 3 s
│   └── stores/
│       ├── telemetry.js   # Pinia store: cpu, ram, temperature, wifi, uptime, connected
│       └── camera.js      # Pinia store for camera state
└── dist/                  # Built frontend — served by FastAPI at runtime
```

### Data flows

- **Telemetry**: browser opens `wss://<host>/ws/telemetry` via `useWebSocket.js` → FastAPI pushes JSON every second from `telemetry_generator()` → Pinia `telemetry` store → `TelemetryPanel`.
- **Camera**: `camera.py` captures frames in a background thread into `latest_frame`; FastAPI streams them as MJPEG via `GET /camera`; `cameraFeed.vue` renders with a plain `<img src="/camera">`.
- **Control**: `ControlPad` sends `POST /api/control {command}` → `routes.py` → `motors.handle_command()`.

### Hardware stubs

`app/hardware/motors.py` currently only prints commands. Real GPIO control (gpiozero is installed) goes here. `app/core/camera.py` opens `/dev/video0` via OpenCV — this will fail if no camera is attached.

### Allowed origins (CORS + WS)

Defined in `app/main.py`:
- `https://raspberrypi.taild8e577.ts.net` (Tailscale hostname)
- `http://localhost:8000`
- `http://100.78.160.76:8000` (LAN IP)

Add new origins here when accessing from a new address.
