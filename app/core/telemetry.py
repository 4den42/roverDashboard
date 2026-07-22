import asyncio
import psutil
import time


def get_cpu_temp() -> float:
    try:
        with open("/sys/class/thermal/thermal_zone0/temp") as f:
            return float(f.read()) / 1000
    except Exception:
        return 0.0


def get_wifi_strength() -> int:
    try:
        with open("/proc/net/wireless") as f:
            for line in f:
                if "wlan0" in line:
                    return int(float(line.split()[3].rstrip(".")))
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

        yield {
            "cpu": cpu,
            "ram": mem.percent,
            "temperature": get_cpu_temp(),
            "wifi": get_wifi_strength(),
            "uptime": int(time.time() - psutil.boot_time()),
            "eth_rx": eth_rx,
            "eth_tx": eth_tx,
        }
        await asyncio.sleep(1)
