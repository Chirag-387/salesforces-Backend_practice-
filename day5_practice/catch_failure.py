import httpx

try:
    response = httpx.get("https://this-site-does-not-exist-12345.com", timeout = 3)
    print(response.status_code)
except httpx.RequestError as error:
    print("The request never completed")
    print(error)

