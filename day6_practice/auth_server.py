from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

app = FastAPI()

class TokenRequest(BaseModel):
    client_id: str
    client_secret: str

@app.post("/token")
def get_token(body: TokenRequest):
    if body.client_id == "my-app" and body.client_secret == "my-secret":
        return {"access_token": "tok_123", "token_type": "Bearer", "expires_in": 3600}
    raise HTTPException(status_code = 401, detail = "Bad credentials")

@app.get("/accounts")
def accounts(authorization: str = Header(default = "")):
    if authorization != "Bearer tok_123":
        raise HTTPException(status_code = 401, detail = "Invalid or missing token")
    return {"accounts": [{"id": 1, "name": "Acme Corp"}]}