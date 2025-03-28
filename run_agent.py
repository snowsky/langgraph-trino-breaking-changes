import os
from my_agent import main

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

# Sleep for an hour to keep the container running
# This is useful if you want to keep the container alive for debugging or other purposes.
import time
time.sleep(3600)
