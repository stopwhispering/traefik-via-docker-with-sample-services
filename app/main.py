import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Hello FastAPI + SSL"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)