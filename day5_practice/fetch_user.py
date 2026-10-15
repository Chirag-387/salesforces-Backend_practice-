import httpx
import time

def fetch_user(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"  
    for attempt in range(1, 4):
        print("Attempt:", attempt)
        try:
            response = httpx.get(url, timeout=3)              
            code = response.status_code
            if 200 <= code < 300:
                return response.json()["name"]               
            if 400 <= code < 500:
                print("Client error, not retrying:", code)
                return None
            print("Not a success, retry:", code)
        except httpx.RequestError as error:
            print("Request never completed:", error)
        if attempt < 3:
            time.sleep(1)
    print("Giving up")
    return None      

print(fetch_user(1))
print(fetch_user(9999))
print(fetch_user(2))