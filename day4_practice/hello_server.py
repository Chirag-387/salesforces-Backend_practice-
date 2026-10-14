from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "hi"}

@app.get("/bulk-jobs")
def jobs():
    return {"jobs": []}