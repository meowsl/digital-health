from sqlalchemy import (
    Column,
    Integer,
    String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import(
    Mapped,
    mapped_column
)
from server.settings import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = Column(Integer, primary_key=True)
    username: Mapped[str] = Column(String(128), unique=True)
    password: Mapped[str] = Column(String)