import httpx
import time

def get_with_retry(url):
    for attempt in range(1, 4):
        print("Attempt:", attempt)
        try:
            response = httpx.get(url, timeout = 3)
            code = response.status_code
            if 200 <= code < 300:
                print("Sucess:", code)
                return
            if 400 <= code < 500:
                print("Client error, not retrying:", code)
                return
            print("Not a success, will retry: ", code)
        except httpx.RequestError as error:
            print("Request never completed:", error)
        if attempt < 3:
            time.sleep(1)
    print("Giving up")


get_with_retry("https://httpbin.org/status/200")
get_with_retry("https://httpbin.org/status/404")
get_with_retry("https://httpbin.org/status/503")
get_with_retry("https://this-site-does-not-exist-12345.com")