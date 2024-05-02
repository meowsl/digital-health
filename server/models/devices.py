from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import(
    Mapped,
    mapped_column,
    relationship
)
from server.settings import Base
from .association_table import user_device_table

class Device(Base):
    '''
    Устройство
    '''
    __tablename__ = "device"

    id: Mapped[int] = Column(Integer, primary_key=True)
    name: Mapped[str] = Column(String(128), unique=True, info={"label": "Название устройства"})

    data = relationship("DeviceData", back_populates="device", cascade="all, delete-orphan")

    users = relationship("User", secondary=user_device_table, back_populates="devices")

class DeviceData(Base):
    '''
    Данные передаваемые с устройства
    '''
    __tablename__ = "device_data"

    id: Mapped[int] = Column(Integer, primary_key=True)
    indicator: Mapped[str] = Column(String(64), info={"label": "Название показателя"})
    unit: Mapped[str] = Column(String(32), info={"label":"Единица измерения"})
    device_id: Mapped[int] = Column(Integer, ForeignKey("device.id"))

    device = relationship("Device", back_populates="data")
