import httpx

response = httpx.get("https://jsonplaceholder.typicode.com/users/1")

if response.status_code == 200:
    data = response.json()
    print(data["name"])
elif response.status_code == 404:
    print("The user wasn't found")
else:
    print(response.status_code)