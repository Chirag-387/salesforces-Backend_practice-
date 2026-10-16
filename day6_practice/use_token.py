import httpx

BASE_URL = "http://127.0.0.1:8000"

# Step 1: log in and get a token
login = httpx.post(
    f"{BASE_URL}/token",
    json={"client_id": "my-app", "client_secret": "my-secret"},
    timeout=3,
)

if login.status_code != 200:
    print("Login failed:", login.status_code)
else:
    token = login.json()["access_token"]

    # Step 2: use the token
    response = httpx.get(
        f"{BASE_URL}/accounts",
        headers={"Authorization": f"Bearer {token}"},
        timeout=3,
    )

    print(response.status_code)
    print(response.json())