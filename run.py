import subprocess
import time

try:
    while True:
        print("Starting main.py...")
        process = subprocess.Popen(["python", "main.py"])

        print("Press Enter to kill and restart...")
        op = input("Press 'q' to quit or any other key to restart: ")
        if op == "q":
            break
        print("Killing main.py...")
        process.terminate()

        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            print("Force killing main.py...")
            process.kill()

        print("Restarting...\n")
        time.sleep(1)
except KeyboardInterrupt:
    process.kill()
    print("\nExiting...")

process.kill()
print("Process killed.")
