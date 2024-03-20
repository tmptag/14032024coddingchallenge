from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import json
from datetime import datetime
from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy.ext.declarative import declarative_base
from modelcreation import (
    Planning,
    Talent,
    Skills,
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
    with open(file_path + "planning.json") as f:
        data = json.load(f)

    # creating session
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()

    talent_dict = {}
    skills_dict = {}
    client_dict = {}
    job_dict = {}

    for record in data:

        # for each record in json data, we are converting it into the datetime format(where necessary).
        record["startDate"] = datetime.strptime(
            record["startDate"], "%m/%d/%Y %I:%M %p"
        )
        record["endDate"] = datetime.strptime(record["endDate"], "%m/%d/%Y %I:%M %p")

        talentName = record["talentName"]

        if talentName not in talent_dict:
            _talent = Talent(
                talentId=record["talentId"],
                talentName=talentName,
                talentGrade=record["talentGrade"],
            )
            session.add(_talent)
            talent_dict[talentName] = _talent
        else:
            _talent = talent_dict[talentName]

        if record["requiredSkills"]:
            for value in record["requiredSkills"]:
                name = value["name"]
                if name not in skills_dict:
                    _name = Skills(
                        name=name,
                        category=value["category"],
                    )
                    skills_dict[name] = _name
                    session.add(_name)

                else:
                    _name = skills_dict[name]

        else:
            name = None

            if name not in skills_dict:
                _name = Skills(name=None, category=None)
                skills_dict[name] = _name
                session.add(_name)

            else:
                _name = skills_dict[name]

        if record["optionalSkills"]:
            for value in record["optionalSkills"]:
                name = value["name"]

                if name not in skills_dict:
                    _name = Skills(name=name, category=value["category"])
                    skills_dict[name] = _name
                    session.add(_name)
                else:
                    _name = skills_dict[name]

        else:
            name = None

            if name not in skills_dict:
                _name = Skills(name=None, category=None)
                skills_dict[name] = _name
                session.add(_name)

            else:
                _name = skills_dict[name]

        # ------
        clientName = record["clientName"]
        print("=====", clientName, type(clientName))

        if clientName not in client_dict:
            client = Client(clientName=clientName)
            client_dict[clientName] = client
            session.add(client)
        else:
            client = client_dict[clientName]
        # ------

        jobManagerName = record["jobManagerName"]

        if jobManagerName not in job_dict:
            _job = Job(
                jobManagerName=jobManagerName, jobManagerId=record["jobManagerId"]
            )
            job_dict[jobManagerName] = _job
            session.add(_job)
        else:
            _job = job_dict[jobManagerName]

        _planning = Planning(
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
            skills=_name,
            client=client,
            job=_job,
        )

        session.add(_planning)

    session.commit()
    session.close()  # closing session.
    print("Data imported successfully.")
except:
    print("error at data importing into the database")
    print(traceback.format_exc())
    # in case of failure make sure that our session is closed, so check if available then close.
    if session:
        session.close()
