"""this modulos contains daos and models for the questions and answers posting"""

from pydantic import BaseModel
from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Float,
    Boolean,
)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv


DATABASE_CONNECTION = "postgresql://postgres:postgres@localhost:5432/modelosbase"

engine = create_engine(DATABASE_CONNECTION)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Session = SessionLocal()
Base = declarative_base()
