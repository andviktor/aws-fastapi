from fastapi import FastAPI
import uvicorn
import platform
import sys

app: FastAPI = FastAPI()

@app.get("/")
async def root() -> dict:
    return {
        "python_version": platform.python_version(),
        "interpreter_path": sys.executable
    }
