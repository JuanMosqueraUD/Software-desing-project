""" Module where web services are defined """
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, SecretStr
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import models
from models import appDAO
from typing import List, Annotated
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

@app.get("/user")
def get_user():
    pass



@app.get("/questions/{question_id}")
def get_question():
    """Get a question by its id"""
    pass

@app.post("/answers/")
def create_answer():
    """Create an answer into the database"""
    pass