from sqlalchemy import (
    Column,
    Integer,
    String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.event import listens_for
from sqlalchemy.orm import(
    Mapped,
    mapped_column,
    relationship
)
from werkzeug.security import generate_password_hash
from server.settings import Base
from .association_table import user_device_table

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = Column(Integer, primary_key=True)
    username: Mapped[str] = Column(String(128), unique=True, info={"label":"Логин"})
    password: Mapped[str] = Column(String, info={"label":"Пароль"})
    email: Mapped[str] = Column(String(128), unique=True, info={"label":"Электронная почта"})
    role: Mapped[str] = Column(String(32), info={"label":"Роль"})

    firstname: Mapped[str] = Column(String(64), info={"label":"Имя"})
    lastname: Mapped[str] = Column(String(64), info={"label":"Фамилия"})
    midname: Mapped[str] = Column(String(64), nullable=True, info={"label":"Отчество"})

    devices = relationship("Device", secondary=user_device_table, back_populates="users")
    measurements = relationship("Measurement", back_populates="user")

    def __str__(self):
        return self.username

@listens_for(User, "before_insert")
def hash_password(mapper, connection, target):
    if target.password != generate_password_hash(target.password):
        target.password = generate_password_hash(target.password)