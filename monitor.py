import psutil
import time
import subprocess

THRESHOLD = 75

def trigger_cloud():
    print("⚠️ CPU > 75%! Starting cloud VM...")
    subprocess.run([
        "gcloud", "compute", "instances", "start", "cloud-vm",
        "--zone", "asia-south1-a"
    ])

while True:
    cpu = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu}%")

    if cpu > THRESHOLD:
        trigger_cloud()
        break

    time.sleep(5)