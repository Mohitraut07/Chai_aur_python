# Exponential Backoff
import time

wait_time = 1 # Time in seconds
max_attempts = 5
attempts = 0

while attempts < max_attempts:
    print("Attempt",attempts+1,"- Wait time",wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
