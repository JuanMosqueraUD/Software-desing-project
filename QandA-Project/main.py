""" Module where web services are defined """

import os
from fastapi import FastAPI
from pydantic import BaseModel, SecretStr
from dotenv import load_dotenv
from sqlalchemy import create_engine

app = FastAPI(
    title="Questions and answers API",
    version="0.1",
    description="API used for conection and storage of a question and answers forum.",
)

