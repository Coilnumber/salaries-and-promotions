from pydantic import BaseModel
from datetime import date

class UserSchema(BaseModel):
    login: str
    name: str
    password: bytes
    salary: int
    date_of_promotion: date
    is_active: bool = True