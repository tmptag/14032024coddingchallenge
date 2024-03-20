from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///./alchemyprac.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


def reload_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print("reload_db Done")


def create_user(session, name: str, age: int):
    user = User(name=name, age=age)
    session.add(user)
    session.commit()
    session.refresh(user)
    session.close()
    print("user created")


# create_user(session, "harry", 25)
# this way of the creating user is as same as the pydantic models user=User(name="herry", age=25)
# for maintaining this database closing connectivity we need to use the support of the yeild keyword and Depends(it is the imported from the fastapi) module, from where we can pass session to our functions.
reload_db()
user = User(name="umg", age=64)
session.add(user)
session.commit()
session.refresh(user)
user = User(name="harry", age=40)
session.add(user)
session.commit()
session.refresh(user)
user = User(name="gerry", age=15)
session.add(user)
session.commit()
session.refresh(user)
user = User(name="kerry", age=25)
session.add(user)
session.commit()
session.refresh(user)
session.close()
print("user created")
