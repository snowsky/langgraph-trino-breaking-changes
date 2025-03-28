import os
import sys
import time
import threading
from my_agent import main

def print_dots():
    """Print dots until the main task finishes."""
    while keep_printing:
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.5)  # Adjust the interval between dots

# Global flag to control the dot-printing thread
keep_printing = True

# Start the dot-printing thread
print("Running: ", end="", flush=True)
dot_thread = threading.Thread(target=print_dots)
dot_thread.start()

try:
    version_start = os.environ["VERSION_START"]
    version_end = os.environ["VERSION_END"]
except KeyError:
    print("Environment variable 'VERSION_START' or 'VERSION_END' is not defined!")
    os._exit(1)
summary, breaking_changes = main(version_start=version_start, version_end=version_end)

print("Summary:")
print(summary)
print("-" * 80)
print("Breaking Changes:")
print(breaking_changes)

# Stop the dot-printing thread when the task is done
keep_printing = False
dot_thread.join()  # Wait for the thread to finish

# Sleep for an hour to keep the container running
# This is useful if you want to keep the container alive for debugging or other purposes.
import time
time.sleep(3600)
