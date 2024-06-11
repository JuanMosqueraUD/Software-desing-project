""" Module where web services are defined """
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, SecretStr
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models
from typing import List, Annotated
app = FastAPI(
    title="Questions and answers API",
    version="0.1",
    description="API used for conection and storage of a question and answers forum.",
)

@app.get("/user")
def get_user():
    pass

models.Base.metadata.create_all(engine)
class User(BaseModel):
    """Model for the user object"""
    username: str
    password: SecretStr
    is_admin: bool

class QuestionBase(BaseModel):
    """Model for the question object"""
    title: str
    body: str
    user_id: int

class AnswerBase(BaseModel):
    """Model for the answer object"""
    body: str
    user_id: int
    question_id: int


def get_db():
    """Get a database session"""
    db = Session()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
