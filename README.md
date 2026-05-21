Rover Dashboard
# Rover Dashboard System (Current Overview)

## Summary

This project is a real-time remote rover control and monitoring system designed to operate securely over a Tailscale network. It provides live telemetry, a camera feed, and remote control capabilities through a web-based dashboard.

---

## Current Features

### 1. Web-Based Dashboard (Vue 3)

* Single-page application interface
* Real-time updates from the rover
* Displays telemetry and camera feed
* Sends control commands to backend services

---

### 2. Backend API (FastAPI on Raspberry Pi)

* WebSocket telemetry stream:

  * `/ws/telemetry`
* REST control interface:

  * `/control`
* Camera streaming endpoint:

  * `/camera`
* Handles communication between frontend and hardware layer

---

### 3. Real-Time Telemetry System

* Continuous data stream from Raspberry Pi to browser
* Uses WebSocket for low-latency updates
* Designed for live sensor and system state monitoring

---

### 4. Camera Streaming

* Live video feed from rover-mounted camera
* Accessible through HTTP endpoint
* Displayed directly in the dashboard UI

---

### 5. Remote Control Interface

* Sends structured commands from frontend to backend
* Backend interprets and forwards commands to hardware layer

---

### 6. Secure Network Access (Tailscale)

* Entire system is accessed through a private Tailscale URL
* No public port forwarding required
* Encrypted tunnel between user device and Raspberry Pi

---

## System Architecture

```
Browser (Vue Dashboard)
        │
        │ HTTPS (Tailscale Secure Tunnel)
        ▼
Raspberry Pi (FastAPI Backend)
   ├── WebSocket: /ws/telemetry
   ├── REST API: /control
   ├── Camera Stream: /camera
   └── Hardware Interface
```

---

## Advantages of This Design

### 1. Low-Latency Real-Time Control

* WebSockets allow near-instant telemetry updates
* Suitable for responsive remote interaction

---

### 2. Single Secure Access Point

* All services are exposed through a single Tailscale URL
* Eliminates need for port forwarding or public exposure

---

### 3. Modular Architecture

* Frontend, backend, and hardware layers are separated
* Each component can be upgraded independently

---

### 4. Remote Operability

* Can be accessed from anywhere inside the Tailscale network
* No dependency on local network proximity

---

### 5. Expandable Design

* Can integrate additional sensors
* Supports future upgrades like autonomy or AI-based control

---

## Intended Use Case

* Remote robotics experimentation
* Real-time embedded system control
* Educational and prototyping platform for rover systems
