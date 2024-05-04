from sqladmin import ModelView
from server.models import Measurement

class MeasurementAdmin(ModelView, model=Measurement):
    name = "Измерениe"
    name_plural = "Измерения"
    icon = "fa fa-chart-line"

    column_list = [
        Measurement.user,
        Measurement.device,
        Measurement.data,
        Measurement.value,
        Measurement.timestamp
    ]
    column_labels ={
        Measurement.user: "Пользователь",
        Measurement.device: "Устройство",
        Measurement.data: "Данные",
        Measurement.value: "Показатель",
        Measurement.timestamp: "Время"
    }
    column_searchable_list = [
        'user.username',
        'device.name',
    ]
