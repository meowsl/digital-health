from pydantic import BaseModel, Field

class DeviceDataBase(BaseModel):
    indicator: str = Field(..., example="Temperature")
    unit: str = Field(..., example="Celsius")

class DeviceData(DeviceDataBase):
    id: int
    device_id: int

    class Config:
        from_attributes = True

class DeviceBase(BaseModel):
    name: str = Field(..., example="Device 1")
    data: list[DeviceDataBase] = Field(
        default=[{
            "indicator": "Temperature",
            "unit": "Celsius"
        }])

class Device(DeviceBase):
    id: int

    class Config:
        from_attributes = True
