import subprocess
import time

while True:
    print("Starting main.py...")
    # Start the subprocess
    process = subprocess.Popen(["python", "main.py"])

    print("Press Enter to kill and restart...")
    input()

    print("Killing main.py...")
    process.terminate()

    try:
        # Wait for the process to terminate
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        print("Force killing main.py...")
        process.kill()

    print("Restarting...\n")
    time.sleep(1)
