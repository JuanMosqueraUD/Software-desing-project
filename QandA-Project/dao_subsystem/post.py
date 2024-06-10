"""this modulos contains daos and models for the questions and answers posting"""

import os
from pydantic import BaseModel
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv


metadata = MetaData()

load_dotenv()

question_db = Table(
    "questions",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("title", String(50)),
    Column("body", String(200)),
    Column("user_id", Integer,forangeinkey=True),
    Column("created_at", String(50)),
    Column("votes", Integer),
)

DATABASE_CONNECTION = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_URL')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
db_conn = create_engine(DATABASE_CONNECTION)
conn = db_conn.connect()
Session = sessionmaker(bind=db_conn)
session = Session()

metadata.create_all(db_conn)

session.commit()

class PostDAO():

    pass
    
        
        