from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    Table,
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

    planning_skill = Table(
        "planning_skill",
        Base.metadata,
        Column("planning_id", ForeignKey("plannings.id"), primary_key=True),
        Column("skill_id", ForeignKey("skills.id"), primary_key=True),
    )

    class Planning(Base):
        __tablename__ = "plannings"

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
        # skill_id = Column(Integer, ForeignKey("skills.id"))
        client_id = Column(Integer, ForeignKey("client.id"))
        job_id = Column(Integer, ForeignKey("job.id"))

        # relationships established from both side.
        talent = relationship("Talent", back_populates="plannings")
        skills = relationship(
            "Skills", secondary="planning_skill", back_populates="plannings"
        )
        client = relationship("Client", back_populates="plannings")
        job = relationship("Job", back_populates="plannings")

    class Talent(Base):
        __tablename__ = "talent"

        id = Column(Integer, primary_key=True)
        talentId = Column(String, nullable=True)
        talentName = Column(String, nullable=True)
        talentGrade = Column(String, nullable=True)

        plannings = relationship("Planning", back_populates="talent")

    class Skills(Base):
        __tablename__ = "skills"

        id = Column(Integer, primary_key=True)
        name = Column(String, nullable=True)
        category = Column(String, nullable=True)

        plannings = relationship(
            "Planning", secondary="planning_skill", back_populates="skills"
        )

    class Client(Base):
        __tablename__ = "client"

        id = Column(Integer, primary_key=True)
        clientName = Column(String, nullable=True)
        clientId = Column(String, nullable=True)

        plannings = relationship("Planning", back_populates="client")

    class Job(Base):
        __tablename__ = "job"

        id = Column(Integer, primary_key=True)
        jobManagerName = Column(String, nullable=True)
        jobManagerId = Column(String, nullable=True)

        plannings = relationship("Planning", back_populates="job")

except:
    print("====Reason for model initialization failure are as follows====")
    print(traceback.format_exc())
