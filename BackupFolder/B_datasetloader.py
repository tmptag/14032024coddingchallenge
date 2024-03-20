from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import json
from datetime import datetime
from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy.ext.declarative import declarative_base
from BackupFolder.B_modelcreation import (
    Planning,
    Talent,
    Rskills,
    Oskills,
    Client,
    Office,
    Job,
    Timming,
    Base,
)
import time
import traceback

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

        planning_record = Planning(
            id=record["id"],
            originalId=record["originalId"],
            bookingGrade=record["bookingGrade"],
            operatingUnit=record["operatingUnit"],
            industry=record["industry"],
            isUnassigned=record["isUnassigned"],
        )

        talent_records = Talent(
            talentId=record["talentId"],
            talentName=record["talentName"],
            talentGrade=record["talentGrade"],
            planning=planning_record,
        )

        rskills_records = Rskills(
            requiredSkills=record["requiredSkills"], planning=planning_record
        )

        oskills_records = Oskills(
            optionalSkills=record["optionalSkills"], planning=planning_record
        )

        client_records = Client(
            clientName=record["clientName"],
            clientId=record["clientId"],
            planning=planning_record,
        )

        office_records = Office(
            officeCity=record["officeCity"],
            officePostalCode=record["officePostalCode"],
            planning=planning_record,
        )

        job_records = Job(
            jobManagerName=record["jobManagerName"],
            jobManagerId=record["jobManagerId"],
            planning=planning_record,
        )

        timming_records = Timming(
            totalHours=record["totalHours"],
            startDate=record["startDate"],
            endDate=record["endDate"],
            planning=planning_record,
        )

        # adding each record.
        session.add(planning_record)
        session.add(talent_records)
        session.add(rskills_records)
        session.add(client_records)
        session.add(office_records)
        session.add(job_records)

    session.commit()
    session.close()  # closing session.
    print("Data imported successfully.")
except:
    print("error at data importing into the database")
    print(traceback.format_exc())
    # in case of failure make sure that our session is closed, so check if available then close.
    if session:
        session.close()
