import asyncio
import random

async def telemetry_generator():
    while True:
        yield {
            "speed": random.randint(0, 12),
            "battery": random.randint(60, 100),
            "temperature": random.randint(25, 50),
            "signal": random.randint(70, 100)
        }

        await asyncio.sleep(1)
