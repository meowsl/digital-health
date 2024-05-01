from sqladmin import ModelView
from server.models import Device, DeviceData

class DeviceAdmin(ModelView, model=Device):
    column_list = [Device.name, Device.data]

class DeviceDataAdmin(ModelView, model=DeviceData):
    column_list = [DeviceData.indicator, DeviceData.unit, DeviceData.device]