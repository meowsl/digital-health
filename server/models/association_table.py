from sqlalchemy import Table, Column, Integer, ForeignKey
from server.settings import Base

user_device_table = Table(
    'user_device',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('device_id', Integer, ForeignKey('device.id'))
)