from pydantic import BaseModel
from typing import List, Union

class UserBase(BaseModel):
    username: str
    password: str

class UserCreate(UserBase):
    email: str
    role: str
    firstname: str
    lastname: str

class UserDevices(BaseModel):
    device_id: List[int]

class UserPublic(BaseModel):
    id: int
    username: str
    email: str
    firstname: Union[str, None] = None
    lastname: Union[str, None] = None

    class Config:
        from_attributes = True

class User(BaseModel):
    id: int
    username: str
    email: str
    role: str
    firstname: str
    lastname: str


    class Config:
        from_attributes = True
