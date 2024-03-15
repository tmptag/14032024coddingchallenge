from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    Boolean,
    JSON,
)
import traceback
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

try:
    Base = declarative_base()

    class Planning(Base):
        __tablename__ = "planning"

        # one primary key is going to connect with all the other tables/models
        id = Column(Integer, primary_key=True, index=True)

        originalId = Column(String, unique=True, index=True)
        bookingGrade = Column(String, nullable=True)
        operatingUnit = Column(String, nullable=False)
        industry = Column(String, nullable=True)
        isUnassigned = Column(Boolean, nullable=False)
        totalHours = Column(Float, nullable=False)
        startDate = Column(DateTime, nullable=False)
        endDate = Column(DateTime, nullable=False)
        officeCity = Column(String, nullable=True)
        officePostalCode = Column(String, nullable=False)

        talent_id = Column(Integer, ForeignKey("talent.id"))
        rskills_id = Column(Integer, ForeignKey("rskills.id"))
        oskills_id = Column(Integer, ForeignKey("oskills.id"))
        client_id = Column(Integer, ForeignKey("client.id"))
        job_id = Column(Integer, ForeignKey("job.id"))

        # relationships established from both side.
        talent = relationship("Talent", back_populates="planning")
        rskills = relationship("Rskills", back_populates="planning")
        oskills = relationship("Oskills", back_populates="planning")
        client = relationship("Client", back_populates="planning")
        job = relationship("Job", back_populates="planning")

    class Talent(Base):
        __tablename__ = "talent"

        id = Column(Integer, primary_key=True)
        talentId = Column(String, nullable=True)
        talentName = Column(String, nullable=True)
        talentGrade = Column(String, nullable=True)

        planning = relationship("Planning", back_populates="talent")

    class Rskills(Base):
        __tablename__ = "rskills"

        id = Column(Integer, primary_key=True)
        requiredSkills = Column(JSON, nullable=True)

        planning = relationship("Planning", back_populates="rskills")

    class Oskills(Base):
        __tablename__ = "oskills"

        id = Column(Integer, primary_key=True)
        optionalSkills = Column(JSON, nullable=True)

        planning = relationship("Planning", back_populates="oskills")

    class Client(Base):
        __tablename__ = "client"

        id = Column(Integer, primary_key=True)
        clientName = Column(String, nullable=True)
        clientId = Column(String, nullable=False)

        planning = relationship("Planning", back_populates="client")

    class Job(Base):
        __tablename__ = "job"

        id = Column(Integer, primary_key=True)
        jobManagerName = Column(String, nullable=True)
        jobManagerId = Column(String, nullable=True)

        planning = relationship("Planning", back_populates="job")

except:
    print("====Reason for model initialization failure are as follows====")
    print(traceback.format_exc())
