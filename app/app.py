from fastapi import FastAPI
import uvicorn

app: FastAPI = FastAPI()

@app.get("/")
async def root() -> dict:
    return {"message": "Welcome to the simple FastAPI application!"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port="8080")