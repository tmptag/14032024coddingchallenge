js1 = [
    {
        "id": 41,
        "originalId": "df3fcf9b",
        "talentId": "tln_7854",
        "talentName": "Mariechen Hoffmann-Hertrampf",
        "talentGrade": "Senior Associate",
        "bookingGrade": "",
        "operatingUnit": "Operating Unit 3",
        "officeCity": "Vechta",
        "officePostalCode": "31707",
        "jobManagerName": "Hans-Friedrich Adolph",
        "jobManagerId": "tln_3931",
        "totalHours": 32.0,
        "startDate": "12/08/2022 11:02 PM",
        "endDate": "12/12/2022 11:02 PM",
        "clientName": "Döhn",
        "clientId": "cl_1",
        "industry": "Low technology",
        "isUnassigned": False,
        "requiredSkills": [],
        "optionalSkills": [{"name": "Javascript", "category": "Coding Language"}],
    }
]

for record in js1:
    print(record)
    if record["requiredSkills"]:
        print("==req", record["requiredSkills"])
    else:
        print("na req")
    if record["optionalSkills"]:
        print("==opt", record["optionalSkills"])


lst = [
    {"name": "TypeScript", "category": "Coding Language"},
    {"name": "Spanish", "category": "Language"},
    {"name": "French", "category": "Language"},
    {"name": "Scala", "category": "Coding Language"},
]
for i, j in enumerate(lst):
    print(i, j)
