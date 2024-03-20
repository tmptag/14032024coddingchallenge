from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
import traceback
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import json
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


# many-to-one type of relationship is going to create here.
try:

    class Person(Base):
        __tablename__ = "person"

        id = Column(Integer, primary_key=True, index=True)
        name = Column(String, nullable=False)
        skill_id = Column(Integer, ForeignKey("skills.id"))

        skills = relationship("Skills", back_populates="person")

    class Skills(Base):
        __tablename__ = "skills"
        id = Column(Integer, primary_key=True, index=True)
        skill_name = Column(String, unique=True)

        person = relationship("Person", back_populates="skills", uselist=False)

    print("Done Modeling")

except:
    print("modeling error reason below")
    print(traceback.format_exc())

session = None

try:
    engine = create_engine("sqlite:///./many_to_one.db")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    sessionlocal = sessionmaker(bind=engine)
    session = sessionlocal()

    # skill_q = session.query(Skills).filter_by(skill_name="swim").first()
    # for ele in skill_q.person:
    #     print("==", ele.name)

    session.close()

    with open("test.json") as f:
        data = json.load(f)

    for record in data:
        person_record = Person(id=record["id"], name=record["name"])
        skill_record = Skills(skill_name=record["skill_name"], person=person_record)
        session.add(person_record)
        session.add(skill_record)

    session.commit()
    session.close()

    print("done database filling")

except:
    print("error in database filling", traceback.format_exc())
    if session:
        session.close()
