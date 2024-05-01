from sqlalchemy import (
    Column,
    Integer,
    String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.event import listens_for
from sqlalchemy.orm import(
    Mapped,
    mapped_column
)
from werkzeug.security import generate_password_hash
from server.settings import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = Column(Integer, primary_key=True)
    username: Mapped[str] = Column(String(128), unique=True, info={"label":"Логин"})
    password: Mapped[str] = Column(String, info={"label":"Пароль"})

@listens_for(User, "before_insert")
def hash_password(mapper, connection, target):
    if target.password != generate_password_hash(target.password):
        target.password = generate_password_hash(target.password)