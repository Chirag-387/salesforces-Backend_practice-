import httpx

response = httpx.post(
    "http://127.0.0.1:8000/token",
    json={"client_id": "my-app", "client_secret": "my-secret"},
    timeout=3,
)

print(response.status_code)
print(response.json())