from sqlalchemy import Boolean, Column, String, ForeignKey, Integer, Table, MetaData
from database import Base



class Questions(Base):
    __tablename__ = "questions"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50))
    body = Column(String(200))
    user_id = Column(Integer, ForeignKey("users.id"))
    votes = Column(Integer)

class Answers(Base):
    __tablename__ = "answers"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    body = Column(String(200))
    user_id = Column(Integer, ForeignKey("users.id"))
    votes = Column(Integer)
    question_id = Column(Integer, ForeignKey("questions.id"))

class Users(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50))
    password = Column(String(50))
    is_admin = Column(Boolean)
    
