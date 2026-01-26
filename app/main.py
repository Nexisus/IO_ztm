from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok", "msg": "Hello from FastAPI + GitHub Actions"}