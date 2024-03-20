from fastapi import FastAPI, Query
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from databases import Database
from typing import Optional
from sqlalchemy.orm import Session
from Dataset.modelcreation import (
    Planning,
    Talent,
    Rskills,
    Oskills,
    Client,
    Job,
    Base,
)
import uvicorn
import time


# establishing the db, if not created then create one(named: test.db) at the root level
# reference taken from: https://www.datacamp.com/tutorial/sqlalchemy-tutorial-examples
# Topic name: Creating Tables

# creating apk for fastapi
app = FastAPI()


engine = Database("sqlite:///./test.db")
SessionLocal = sessionmaker(bind=engine)


@app.get("/planning123/")
async def get_planning(
    skip_records: int = Query(0, ge=0),
    records_in_one_page: int = Query(10, le=100),
    sort_by: Optional[str] = Query(None, pattern=r"^[a-zA-Z_][a-zA-Z0-9_]*$"),
    isUnassigned: Optional[bool] = None,
):

    try:
        db = SessionLocal()

        # person_obj = (
        #     query(Planning).join(Rskills).filter(Planning.rskills_id == Rskills.id).all()
        # )

        if sort_by:
            query = db.query.order_by(getattr(Planning, sort_by))
            pagination_query = query.offset(skip_records).limit(records_in_one_page)
        else:
            pagination_query = db.query.offset(skip_records).limit(records_in_one_page)

        return pagination_query.all()
    finally:
        if db:
            db.close()


if __name__ == "__main__":
    uvicorn.run(app, port=9000)
