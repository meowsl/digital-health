from pydantic import BaseModel
from typing import List

class UserBase(BaseModel):
    username: str
    password: str

class UserCreate(UserBase):
    email: str
    firstname: str
    lastname: str
    role: str

class UserDevices(BaseModel):
    device_id: List[int]

class User(BaseModel):
    id: int
    username: str
    email: str
    role: str

    class Config:
        from_attributes = True