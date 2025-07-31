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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port="8080")