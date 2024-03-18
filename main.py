from fastapi import FastAPI, HTTPException, Query, Depends
from typing import List
from Dataset.schemas import PlanningP, SkillsP
from Dataset._modelcreation import Planning, Skills
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import uvicorn
from sqlalchemy.orm import Session
from typing import Optional

# Initialize FastAPI app
app = FastAPI()

# SQLAlchemy engine setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.get("/skills/", response_model=List[SkillsP])
# async def get_all_skills(db=Depends(get_db)):
#     skills = db.query(Skills).all()
#     return skills


@app.get("/planning/", response_model=List[PlanningP])
async def get_all_planning_data(
    skip: int = Query(0, ge=0),
    limit_per_page: int = Query(10, le=100),
    sort_by: Optional[str] = Query(None, pattern=r"^[a-zA-Z_][a-zA-Z0-9_]*$"),
    db: Session = Depends(get_db),
):
    query = db.query(Planning)

    if sort_by is not None:
        query = query.order_by(getattr(Planning, sort_by))

    planning_data = query.offset(skip).limit(limit_per_page).all()

    return planning_data


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
