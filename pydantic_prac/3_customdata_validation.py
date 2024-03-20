"""
you should import validator from pydantic manually.
"""

from pydantic import BaseModel, validator


class User(BaseModel):
    name: str
    age: int

    @validator("age")
    def validation_example(cls, a):
        if a < 25:
            raise ValueError("age should be > 25")
        return a


d2 = {"name": "h", "age": 26}
person = User(**d2)
print("===d2", person)
d3 = {"name": "h", "age": 18}
person = User(**d3)
print("===d3", person)
