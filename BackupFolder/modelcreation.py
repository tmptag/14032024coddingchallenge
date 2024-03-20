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


try:
    Base = declarative_base()

    class Planning(Base):
        __tablename__ = "planning"

        id = Column(Integer, primary_key=True, index=True)
        originalId = Column(String, unique=True, index=True)
        talentId = Column(String, nullable=True)
        talentName = Column(String, nullable=True)
        talentGrade = Column(String, nullable=True)
        bookingGrade = Column(String, nullable=True)
        operatingUnit = Column(String, nullable=False)
        officeCity = Column(String, nullable=True)
        officePostalCode = Column(String, nullable=False)
        jobManagerName = Column(String, nullable=True)
        jobManagerId = Column(String, nullable=True)
        totalHours = Column(Float, nullable=False)
        startDate = Column(DateTime, nullable=False)
        endDate = Column(DateTime, nullable=False)
        clientName = Column(String, nullable=True)
        clientId = Column(String, nullable=False)
        industry = Column(String, nullable=True)
        isUnassigned = Column(Boolean, nullable=False)
        requiredSkills = Column(JSON, nullable=True)
        optionalSkills = Column(JSON, nullable=True)

except:
    print("====Reason for model initialization failure are as follows====")
    print(traceback.format_exc())
