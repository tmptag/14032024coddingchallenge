import json
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import traceback

Base = declarative_base()


class Person(Base):
    __tablename__ = "person"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    skill_id = Column(Integer, ForeignKey("skill.id"))
    skill = relationship("Skill", back_populates="people")


class Skill(Base):
    __tablename__ = "skill"
    id = Column(Integer, primary_key=True)
    skill_name = Column(String)
    people = relationship("Person", back_populates="skill")


engine = create_engine("sqlite:///test.db")
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

with open("test.json") as f:
    data = json.load(f)

try:
    skills_dict = {}

    for entry in data:
        skill_name = entry["skill_name"]
        if skill_name not in skills_dict:
            skill = Skill(skill_name=skill_name)
            session.add(skill)
            skills_dict[skill_name] = skill
        else:
            skill = skills_dict[skill_name]

        person = Person(name=entry["name"], skill=skill)
        session.add(person)
    session.commit()
    del skills_dict
    print("Data loaded successfully.")
except Exception as e:
    print("Error:", e)
    print(traceback.format_exc())
    if session:
        session.rollback()
    session.close()
