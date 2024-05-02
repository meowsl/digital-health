from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    DateTime,
    ForeignKey
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)
from server.settings import Base
from server.models import (
    User,
    Device,
    DeviceData
)

class Measurement(Base):
    __tablename__ = "measurements"

    id: Mapped[int] = Column(Integer, primary_key=True)
    user_id: Mapped[int] = Column(Integer, ForeignKey('users.id'))
    device_id: Mapped[int] = Column(Integer, ForeignKey('device.id'))
    data_id: Mapped[int] = Column(Integer, ForeignKey('device_data.id'))
    value: Mapped[float] = Column(Float, nullable=False)
    timestamp: Mapped[DateTime] = Column(DateTime, nullable=False)

    user = relationship(User, back_populates="measurements")
    device = relationship(Device, back_populates="measurements")
    data = relationship(DeviceData, back_populates="measurements")