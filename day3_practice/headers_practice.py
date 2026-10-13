import httpx

url = "https://httpbin.org/bearer"

response = httpx.get(url)
print(response.status_code)

response = httpx.get(url, headers={"Authorization": "Bearer my-practice-token"})
print(response.status_code)
print(response.json())