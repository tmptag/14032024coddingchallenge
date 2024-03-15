from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import json
from datetime import datetime
from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy.ext.declarative import declarative_base
from Dataset._modelcreation import (
    Planning,
    Talent,
    Rskills,
    Oskills,
    Client,
    Job,
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

    talent_dict = {}
    rskills_dict = {}
    oskills_dict = {}
    client_dict = {}
    job_dict = {}

    for record in data:

        # for each record in json data, we are converting it into the datetime format(where necessary).
        record["startDate"] = datetime.strptime(
            record["startDate"], "%m/%d/%Y %I:%M %p"
        )
        record["endDate"] = datetime.strptime(record["endDate"], "%m/%d/%Y %I:%M %p")

        talentName = data["talentName"]

        if talentName not in talent_dict:
            _talent = Talent(
                talentId=record["talentId"],
                talentName=talentName,
                talentName=record["talentName"],
                talentGrade=record["talentGrade"],
            )
            session.add(_talent)
            talent_dict[talentName] = _talent
        else:
            _talent = talent_dict[talentName]

        requiredSkills = record["requiredSkills"]

        if requiredSkills not in rskills_dict:
            _rskills = Rskills(requiredSkills=requiredSkills)
            rskills_dict[requiredSkills] = _rskills
            session.add(_rskills)
        else:
            _rskills = rskills_dict[requiredSkills]

        optionalSkills = record["optionalSkills"]

        if optionalSkills not in oskills_dict:
            _oskills = Oskills(optionalSkills=optionalSkills)
            oskills_dict[optionalSkills] = _oskills
            session.add(_oskills)
        else:
            _oskills = oskills_dict["optionalSkills"]
        # ------
        clientName = record["clientName"]

        if clientName not in client_dict:
            _client = Client(clientName=clientName)
            client_dict[client_dict] = _client
            session.add(_client)
        else:
            _client = client_dict[client_dict]
        # ------

        jobManagerName = record["jobManagerName"]

        if jobManagerName not in client_dict:
            _job = Job(
                jobManagerName=jobManagerName, jobManagerId=record["jobManagerId"]
            )
            job_dict[jobManagerName] = _job
            session.add(_job)
        else:
            _job = job_dict[jobManagerName]

        planning = Planning(
            id=record["id"],
            originalId=record["originalId"],
            bookingGrade=record["bookingGrade"],
            operatingUnit=record["operatingUnit"],
            industry=record["industry"],
            isUnassigned=record["isUnassigned"],
            totalHours=record["totalHours"],
            startDate=record["startDate"],
            endDate=record["endDate"],
            officeCity=record["officeCity"],
            officePostalCode=record["officePostalCode"],
            talent=_talent,
            rskills=_rskills,
            oskills=_oskills,
            client=_client,
            job=_job,
        )

    session.commit()
    session.close()  # closing session.
    print("Data imported successfully.")
except:
    print("error at data importing into the database")
    print(traceback.format_exc())
    # in case of failure make sure that our session is closed, so check if available then close.
    if session:
        session.close()
