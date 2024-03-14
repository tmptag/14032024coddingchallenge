from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import json
from datetime import datetime
from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy.ext.declarative import declarative_base
from modelcreation import Planning, Base

session = None  # making ession None initially to handle the exception.

try:
    # files for loading into the dataset are available at the following path.
    file_path = os.getcwd()
    file_path = file_path + "/Dataset/"

    # establishing the db, if not created then create one(named: test.db) at the root level
    # reference taken from: https://www.datacamp.com/tutorial/sqlalchemy-tutorial-examples
    # Topic name: Creating Tables
    engine = create_engine("sqlite:///./test.db")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    # opening Json file.
    with open(file_path + "_planning.json") as f:
        data = json.load(f)

    # creating session
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()

    for record in data:
        # for each record in json data, we are converting it into the datetime format(where necessary).
        record["startDate"] = datetime.strptime(
            record["startDate"], "%m/%d/%Y %I:%M %p"
        )
        record["endDate"] = datetime.strptime(record["endDate"], "%m/%d/%Y %I:%M %p")

        # validating each record.
        db_record = Planning(**record)
        # adding each record.
        session.add(db_record)

    session.commit()
    session.close()  # closing session.
    print("Data imported successfully.")
except:
    # in case of failure make sure that our session is closed, so check if available then close.
    if session:
        session.close
