import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print(f"Attempt {attempts + 1} of {wait_time} seconds...")
    time.sleep(wait_time)
    attempts += 1
    wait_time *= 2  # Exponential backoff