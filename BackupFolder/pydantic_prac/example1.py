from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: int
    email: str


person = User(name="tanmay", age=26, email="tanmay.111")

# print(person)
# print(person.dict())  # Convert the model to a dictionary
# print(person.name)
# print(person.age)
# print(person.email)


# 2) unpacking dict
d2 = {"name": "dfg", "age": 25, "email": "dfsd.com"}
person = User(**d2)
print(person)
