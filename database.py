from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://todo_trjd_user:wnGdJyL1x9uojDk19YIAHkqNIdCeVv82@dpg-cqumscij1k6c73di53pg-a.singapore-postgres.render.com/todo_trjd"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
