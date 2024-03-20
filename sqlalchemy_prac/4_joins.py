from sqlalchemy import (
    create_engine,
    MetaData,
    Column,
    Integer,
    String,
    ForeignKey,
    text,
)
from sqlalchemy.engine import result
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
# establish connections
engine = create_engine("sqlite:///./alchamyprac.db")

# initialize the Metadata Object
meta = MetaData(bind=engine)
MetaData.reflect(meta)


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


statement = text("select * from cars")
res = engine.execute(statement)
for row in res:
    print(res)
