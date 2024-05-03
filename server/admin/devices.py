from sqladmin import ModelView
from server.models import Device, DeviceData

class DeviceAdmin(ModelView, model=Device):
    name = "Устройство"
    name_plural = "Устройства"
    icon = "fa-solid fa-mobile"

    column_list = [Device.name, Device.data]
    column_labels = {
        Device.name: "Название",
        Device.data: "Передаваемые данные"
    }

class DeviceDataAdmin(ModelView, model=DeviceData):
    name = "Данные"
    name_plural = "Данные"
    icon = "fa-solid fa-table"

    column_list = [DeviceData.indicator, DeviceData.unit, DeviceData.device]
    column_labels = {
        DeviceData.indicator: "Данные",
        DeviceData.unit: "СИ",
        DeviceData.device: "Устройство"
    }