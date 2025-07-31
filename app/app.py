from fastapi import FastAPI
import platform
import sys
import os
from logging import Logger

app: FastAPI = FastAPI()
logger: Logger = Logger(__name__)

@app.get("/")
async def root() -> dict:
    TEST_SECRET = os.getenv("TEST_SECRET", "NO SECRET")
    logger.error(f"TEST_SECRET: {TEST_SECRET}")
    return {
        "python_version": platform.python_version(),
        "interpreter_path": sys.executable
    }
