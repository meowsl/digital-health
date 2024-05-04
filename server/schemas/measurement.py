from pydantic import BaseModel
from datetime import datetime

class MeasurementCreate(BaseModel):
    device_id: int
    data_id: int
    value: float
    timestamp: datetime

class Measurement(BaseModel):
    id: int
    user_id: int
    device_id: int
    data_id: int
    value: float
    timestamp: datetime

    class Config:
        from_attributes = True