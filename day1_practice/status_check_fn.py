import httpx

def check_user(user_id):
    response = httpx.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    if response.status_code == 200:
        data = response.json()
        print(data["name"])
    elif response.status_code == 404:
        print("user wasn't found")
    else:
        print(response.status_code)

check_user(1)
check_user(9999)
check_user(2)