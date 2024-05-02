from pydantic import BaseModel
from typing import List

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserDevices(BaseModel):
    device_id: List[int]

class User(UserBase):
    id: int

    class Config:
        from_attributes = True