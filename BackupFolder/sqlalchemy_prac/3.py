from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Boolean,
    Float,
    ForeignKey,
    DateTime,
)
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///./alchamyprac.db")
Session = sessionmaker(bind=engine)
session = Session()
from sqlalchemy import text

Base = declarative_base()


class Cars(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True)
    car_name = Column(String)
    car_color_id = Column(Integer, ForeignKey("colors.id"))

    colors = relationship("Colors", back_populates="cars")


class Colors(Base):
    __tablename__ = "colors"
    id = Column(Integer, primary_key=True)
    color_name = Column(String)

    cars = relationship("Cars", back_populates="colors")


# obj = session.query(Cars)
# obj_lst = session.query(Cars).join(Colors, Cars.car_color_id == Colors.id).all()
query = session.query(Cars)
obj = query.join(Cars.colors)

for record in obj:
    print(record.car_name)
    print(record.colors)
    print()

"""
select * from left_table
"""
