from fastapi import FastAPI, Query, Depends
from typing import List
from Dataset.schemas import PlanningP
from Dataset._modelcreation import Planning, Skills, Talent, Client, Job
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
import uvicorn
from sqlalchemy.orm import Session
from typing import Optional

app = FastAPI()


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/planning/", response_model=list[PlanningP])
async def get_all_planning_data(
    skip: int = Query(0, ge=0),
    limit_per_page: int = Query(10, le=100),
    sort_by: Optional[str] = Query(None, pattern=r"^[a-zA-Z_][a-zA-Z0-9_]*$"),
    search_query: Optional[str] = None,
    db: Session = Depends(get_db),
):
    query = db.query(Planning)

    if sort_by is not None:
        query = query.order_by(getattr(Planning, sort_by))

    if search_query:
        search_filters = []
        for column in Planning.__table__.columns:
            search_filters.append(column == search_query)

        search_filters += [
            Talent.talentId.ilike(f"%{search_query}%"),
            Talent.talentName.ilike(f"%{search_query}%"),
            Talent.talentGrade.ilike(f"%{search_query}%"),
            Skills.name.ilike(f"%{search_query}%"),
            Skills.category.ilike(f"%{search_query}%"),
            Client.clientName.ilike(f"%{search_query}%"),
            Client.clientId.ilike(f"%{search_query}%"),
            Job.jobManagerName.ilike(f"%{search_query}%"),
            Job.jobManagerId.ilike(f"%{search_query}%"),
        ]

        query = (
            query.join(Planning.talent)
            .join(Planning.skills)
            .join(Planning.client)
            .join(Planning.job)
        )

        query = query.filter(or_(*search_filters))

    planning_data = query.offset(skip).limit(limit_per_page).all()

    return planning_data


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
