import httpx

url = "https://httpbin.org/bearer"

def check_token(token):

    if token == "":
        print("No token is given")
        return

    response = httpx.get(url, headers = {"Authorization": f"Bearer {token}"})

    if(response.status_code == 200):
        print("Authenticated")
    elif(response.status_code == 401):
        print("Not authenticated")
    else:
        print(response.status_code)

check_token("abc123")
check_token("")