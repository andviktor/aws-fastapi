from fastapi import FastAPI
import platform
import sys
import os
from logging import Logger
import boto3

app: FastAPI = FastAPI()
logger: Logger = Logger(__name__)

@app.get("/")
async def root() -> dict:
    #get_secret()
    return {
        "secret": os.getenv("TEST_SECRET", "No secret found"),
        "python_version": platform.python_version(),
        "interpreter_path": sys.executable
    }


# def get_secret():

#     secret_name = "ai-article-generator-secrets"
#     region_name = "us-east-1"

#     session = boto3.session.Session()
#     client = session.client(
#         service_name='secretsmanager',
#         region_name=region_name
#     )

#     try:
#         get_secret_value_response = client.get_secret_value(
#             SecretId=secret_name
#         )
#     except Exception as e:
#         raise e

#     secret = get_secret_value_response['TEST_SECRET']
#     logger.error(f"Retrieved secret: {secret}")