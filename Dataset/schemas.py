from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from typing import Union, List

# Note: incase of python's version issue try to run that with the union package of the python.


# class PlanningSkill(BaseModel):
#     planning_id: int
#     skill_id: int

#     class Config:
#         orm_mode = True


class TalentP(BaseModel):
    talentId: Optional[str]
    talentName: Optional[str]
    talentGrade: Optional[str]


class SkillsP(BaseModel):
    name: Optional[str]
    category: Optional[str]


class ClientP(BaseModel):
    clientName: Optional[str]
    clientId: Optional[str]


class JobP(BaseModel):
    jobManagerName: Optional[str]
    jobManagerId: Optional[str]


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
    # skill_id: int
    client_id: int
    job_id: int
    talent: Union[TalentP, None] = None
    skills: Union[List[SkillsP], None] = None
    client: Union[ClientP, None] = None
    job: Union[JobP, None] = None
