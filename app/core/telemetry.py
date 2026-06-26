import asyncio
import psutil
import time


async def get_cpu_temp():
    try:
        proc = await asyncio.create_subprocess_exec(
            "vcgencmd", "measure_temp",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.DEVNULL,
        )
        stdout, _ = await proc.communicate()
        return float(stdout.decode().replace("temp=", "").replace("'C\n", "").strip())
    except Exception:
        return 0.0


async def get_wifi_strength():
    try:
        proc = await asyncio.create_subprocess_exec(
            "iwconfig", "wlan0",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.DEVNULL,
        )
        stdout, _ = await proc.communicate()
        for line in stdout.decode().split("\n"):
            if "Signal level" in line:
                return int(line.split("Signal level=")[1].split(" ")[0])
    except Exception:
        pass
    return 0


async def telemetry_generator():
    prev_net = psutil.net_io_counters(pernic=True).get("eth0")
    prev_net_time = time.monotonic()

    while True:
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory()

        cur_net = psutil.net_io_counters(pernic=True).get("eth0")
        cur_time = time.monotonic()
        eth_rx = eth_tx = 0.0
        if prev_net and cur_net:
            elapsed = cur_time - prev_net_time
            if elapsed > 0:
                eth_rx = round((cur_net.bytes_recv - prev_net.bytes_recv) / elapsed / 1024, 1)
                eth_tx = round((cur_net.bytes_sent - prev_net.bytes_sent) / elapsed / 1024, 1)
        prev_net = cur_net
        prev_net_time = cur_time

        data = {
            "cpu": cpu,
            "ram": mem.percent,
            "temperature": await get_cpu_temp(),
            "wifi": await get_wifi_strength(),
            "uptime": int(time.time() - psutil.boot_time()),
            "eth_rx": eth_rx,
            "eth_tx": eth_tx,
        }

        yield data
        await asyncio.sleep(1)
