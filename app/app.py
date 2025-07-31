from fastapi import FastAPI
import platform
import sys
from logging import Logger

app: FastAPI = FastAPI()
logger: Logger = Logger(__name__)

@app.get("/")
async def root() -> dict:
    logger.error("LOGGER TEST!")
    return {
        "python_version": platform.python_version(),
        "interpreter_path": sys.executable
    }
