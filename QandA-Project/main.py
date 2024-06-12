""" Module where web services are defined """

from typing import Annotated
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine
import models
from models import appDAO

app = FastAPI(
    title="QuestPI",
    version="0.1",
    description="API used for conection and storage of a question and answers forum.",
)


models.Base.metadata.create_all(engine)


def get_db():
    """Get a database session"""
    db = Session()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


@app.post("/questions/create")
def create_question(question: models.QuestionBase):
    """Create a question into the database"""
    appDAO.add_question(question)
    return {"message": "question created successfully"}


@app.get("/user/get")
def get_user():
    return {"message": "user retrieved successfully"}


@app.get("/questions/get")
def get_question():
    """Get a question by its id"""
    return {"message": "question retrieved successfully"}


@app.post("/answers/")
def create_answer():
    """Create an answer into the database"""
    return {"message": "answer created successfully"}


@app.post("/users/create")
def create_user(user: models.UserBase):
    """Create an user into the database"""
    appDAO.add_user(user)
    return {"message": "user created successfully"}
