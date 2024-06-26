"""module used to define the database tables and also create daos for the questions and answers"""

from sqlalchemy import Boolean, Column, String, ForeignKey, Integer, Table, MetaData
from database import Base, Session
from pydantic import BaseModel, SecretStr

metadata = MetaData()


class Questions(Base):
    __tablename__ = "questions"
    metadata
    id = Column(Integer, primary_key=True, autoincrement=True)
    tittle = Column(String(50))
    body = Column(String(200))
    user_id = Column(Integer, ForeignKey("users.id"))
    votes = Column(Integer)


class Answers(Base):
    __tablename__ = "answers"
    metadata
    id = Column(Integer, primary_key=True, autoincrement=True)
    body = Column(String(200))
    user_id = Column(Integer, ForeignKey("users.id"))
    votes = Column(Integer)
    question_id = Column(Integer, ForeignKey("questions.id"))


class Users(Base):
    __tablename__ = "users"
    metadata
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50))
    password = Column(String(50))
    is_admin = Column(Boolean)


class UserBase(BaseModel):
    """Model for the user object"""

    username: str
    password: SecretStr
    is_admin: bool


class QuestionBase(BaseModel):
    """Model for the question object"""

    tittle: str
    body: str
    user_id: int
    votes: int


class AnswerBase(BaseModel):
    """Model for the answer object"""

    body: str
    user_id: int
    question_id: int


class appDAO:
    """this class is to represent the daos for the project"""

    @classmethod
    def add_question(self, question: QuestionBase):
        """This is a method to add questions to database"""
        print(question)
        query = Questions.insert().values(
            title=question.tittle,
            body=question.body,
            user_id=question.user_id,
            votes=question.votes,
        )
        Session.execute(query)
        Session.commit()

    @classmethod
    def add_user(self, user: UserBase):
        """This is a method to add a user"""
        print(user)
        query = Users.insert().values(
            username=user.username,
            password=user.password,
            is_admin=user.is_admin,
        )
        Session.execute(query)
        Session.commit()
