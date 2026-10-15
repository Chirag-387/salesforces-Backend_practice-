import time

def flaky(attempt):
    return attempt >= 3

for attempt in range(1, 4):
    print("Attempt ", attempt)
    if flaky(attempt):
       print("Success")
       break
    print("Failed, waiting 1 second")
    time.sleep(1)