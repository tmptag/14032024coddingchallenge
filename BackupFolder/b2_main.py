from fastapi import FastAPI, Query
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Optional
from Dataset.modelcreation import Planning, Talent, Skills, Client, Job
import uvicorn
import time
import traceback
from pydantic import BaseModel
from typing import Union
from datetime import datetime


class PlanningP(BaseModel):
    id: int
    originalId: str
    bookingGrade: Union[str, None] = None
    operatingUnit: str
    industry: Union[str, None] = None
    isUnassigned: bool
    totalHours: float
    startDate: datetime
    endDate: datetime
    officeCity: Union[str, None] = None
    officePostalCode: str
    talent_id: int
    skill_id: int
    client_id: int
    job_id: int


# Define SQLAlchemy engine globally
engine = create_engine("sqlite:///./test.db")
Session = sessionmaker(bind=engine)

app = FastAPI()


@app.get("/planning123/")
async def get_planning(
    skip_records: int = Query(0, ge=0),
    records_in_one_page: int = Query(10, le=100),
    sort_by: Optional[str] = Query(None, pattern=r"^[a-zA-Z_][a-zA-Z0-9_]*$"),
    isUnassigned: Optional[bool] = None,
):
    # Create a new session for this request
    session = Session()

    try:
        planning_query = session.query(Planning).all()

        validated_data = []

        for planning in planning_query:
            try:
                # Create an instance of the Pydantic model with data from the Planning object
                model_instance = PlanningP(
                    id=planning.id,
                    originalId=planning.originalId,
                    bookingGrade=planning.bookingGrade,
                    operatingUnit=planning.operatingUnit,
                    industry=planning.industry,
                    isUnassigned=planning.isUnassigned,
                    totalHours=planning.totalHours,
                    startDate=planning.startDate,
                    endDate=planning.endDate,
                    officeCity=planning.officeCity,
                    officePostalCode=planning.officePostalCode,
                    talent_id=planning.talent_id,
                    skill_id=planning.skill_id,
                    client_id=planning.client_id,
                    job_id=planning.job_id,
                )
                # Validate the data
                validation_result = model_instance.validate()

                validated_data.append((model_instance, validation_result))
            except Exception as e:
                # If validation fails, append a tuple with the Planning object and the error message
                validated_data.append((planning, str(e)))

        # Return the validated data
        print("===here is the validated_data")
        time.sleep(5)
        print(validated_data)
        return validated_data
    finally:
        # Ensure session is closed even if an exception occurs
        print("==")
        print(traceback.format_exc())
        print("==")
        session.close()


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
