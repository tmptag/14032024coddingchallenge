from fastapi import FastAPI, Query
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Float,
    DateTime,
    Boolean,
    JSON,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database
from typing import Optional
from fastapi import FastAPI, Query, Depends
from sqlalchemy.orm import Session
from Dataset.modelcreation import Planning, Base
import uvicorn


# establishing the db, if not created then create one(named: test.db) at the root level
# reference taken from: https://www.datacamp.com/tutorial/sqlalchemy-tutorial-examples
# Topic name: Creating Tables
engine = create_engine("sqlite:///./test.db")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

# creating apk for fastapi
app = FastAPI()


database = Database("sqlite:///./test.db")


# database closing.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/planning/")
async def get_planning(
    skip_records: int = Query(0, ge=0),
    records_in_one_page: int = Query(10, le=100),
    sort_by: Optional[str] = Query(None, pattern=r"^[a-zA-Z_][a-zA-Z0-9_]*$"),
    db: Session = Depends(get_db),
):
    query = db.query(Planning)

    if sort_by:
        query = query.order_by(getattr(Planning, sort_by))

    query = query.offset(skip_records).limit(records_in_one_page)
    return query.all()


if __name__ == "__main__":
    uvicorn.run(app, port=8000)
