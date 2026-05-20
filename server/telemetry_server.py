import asyncio
import websockets
import json
import random

async def telemetry(websocket):
    while True:
        data = {
            'speed': random.randint(0, 15),
            'battery': random.randint(60, 100),
            'temperature': random.randint(30, 50),
            'signalStrength': random.randint(70, 100),
            'cpuUsage': random.randint(10, 90)
        }

        await websocket.send(json.dumps(data))
        await asyncio.sleep(1)

async def main():
    async with websockets.serve(telemetry, '0.0.0.0', 8765):
        await asyncio.Future()

asyncio.run(main())
