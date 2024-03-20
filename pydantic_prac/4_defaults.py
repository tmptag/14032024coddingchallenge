# in this given example we will can set the default value so there will be three cases 
# 1 where we do not send the value and it will take the by default values that are already definded
# 2 we will give value and it passed the validation
# 3 same in 2 but fail the validation

from pydantic import BaseModel, validator


class Book(BaseModel):
    name: str
    year: int = 2022

    @validator("year")
    def validate(cls, y):
        if y not in range(2000, 2100):
            raise ValueError("outside the book range")
        return y


d1 = {"name": "the secret", "year": 2022}
d2 = {"name": "the secret", "year": 2225}
book = Book(**d1)

print("===Book", book)
