from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi import Depends


engine = create_engine("sqlite:///./alchemyprac.db")
Session = sessionmaker(bind=engine)
Base = declarative_base()


def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


def reload_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print("db deleted and reloaded")


def create_user(name: str, age: int, session: Session = Depends(get_session)):
    user = User(name=name, age=age)



create_user("abhi", 25)
