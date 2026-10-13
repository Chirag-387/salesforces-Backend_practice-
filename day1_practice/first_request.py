import httpx

response = httpx.get("https://jsonplaceholder.typicode.com/users/1")

print(response.status_code)
print(response.headers["content-type"])

data = response.json()
print(data["name"])
print(data["address"]["city"])