import asyncio
import psutil
import os
import time

def get_cpu_temp():
    try:
        return float(
            os.popen("vcgencmd measure_temp").readline()
            .replace("temp=", "")
            .replace("'C\n", "")
        )
    except:
        return 0.0

def get_wifi_strength():
    try:
        result = os.popen("iwconfig wlan0").read()
        for line in result.split("\n"):
            if "Signal level" in line:
                return int(line.split("Signal level=")[1].split(" ")[0])
    except:
        pass
    return 0

async def telemetry_generator():
    while True:
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory()

        data = {
            "cpu": cpu,
            "ram": mem.percent,
            "temperature": get_cpu_temp(),
            "wifi": get_wifi_strength(),
            "uptime": int(time.time() - psutil.boot_time())
        }

        yield data
        await asyncio.sleep(1)
