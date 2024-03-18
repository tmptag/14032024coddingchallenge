from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Note: incase of python's version issue try to run that with the union package of the python.


class PlanningP(BaseModel):
    id: int
    originalId: str
    bookingGrade: Optional[str]
    operatingUnit: str
    industry: Optional[str]
    isUnassigned: bool
    totalHours: float
    startDate: datetime
    endDate: datetime
    officeCity: Optional[str]
    officePostalCode: str
    talent_id: int
    skill_id: int
    client_id: int
    job_id: int


class TalentP(BaseModel):
    id: int
    talentId: Optional[str]
    talentName: Optional[str]
    talentGrade: Optional[str]


class SkillsP(BaseModel):
    id: int
    name: Optional[str]
    category: Optional[str]


class ClientP(BaseModel):
    id: int
    clientName: Optional[str]
    clientId: Optional[str]


class JobP(BaseModel):
    id: int
    jobManagerName: Optional[str]
    jobManagerId: Optional[str]
