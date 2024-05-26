from sqlalchemy.orm import Session
import server.models as models
import server.schemas as schemas
from .user import get_user
from .measurement import get_user_measurements
from datetime import datetime, timedelta
from random import randint, uniform

def ws_get_user_devices(db: Session, user_id: int):
    '''
    Получение всех устройств пользователя
    '''
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # формируем список из имен устройств
    devices_names = [device.name for device in user.devices]

    return devices_names


def ws_generate_measurements_steps(db: Session, user_id: int, device_id: int):
    '''
    Генерация измерений шагомера
    '''
    # Находим устройство и пользователя по их id
    device = db.query(models.Device).filter(models.Device.id == device_id).first()
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not device or not user:
        print("Устройство или пользователь не найдены")
        return

    # Генерируем измерения за прошедшие несколько дней, включая сегодняшний день
    for i in range(4):
        # Генерируем случайное время в течение дня
        time = datetime.combine(datetime.today() - timedelta(days=i), datetime.min.time()) + timedelta(seconds=randint(0, 86400))
        # Генерируем случайное значение value в диапазоне от 1000 до 15000
        value = randint(1000, 15000)

        # Создаем новое измерение и добавляем его в базу данных
        measurement = models.Measurement(user_id=user.id, device_id=device.id, value=value, timestamp=time)
        db.add(measurement)

    # Сохраняем изменения в базе данных
    db.commit()

def ws_generate_measurements_pulse(db: Session, user_id: int, device_id: int):
    '''
    Генерация измерений пульсометра
    '''
    # Находим устройство и пользователя по их id
    device = db.query(models.Device).filter(models.Device.id == device_id).first()
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if not device or not user:
        print("Устройство или пользователь не найдены")
        return

    # Генерируем измерения за прошедшие несколько дней, включая сегодняшний день
    for i in range(4):
        # Генерируем случайное время в течение дня
        time = datetime.combine(datetime.today() - timedelta(days=i), datetime.min.time()) + timedelta(seconds=randint(0, 86400))
        # Генерируем случайное значение value в диапазоне от 60.0 до 100.0 с одним символом после запятой
        value = round(uniform(60.0, 100.0), 1)

        # Создаем новое измерение и добавляем его в базу данных
        measurement = models.Measurement(user_id=user.id, device_id=device.id, value=value, timestamp=time)
        db.add(measurement)

    # Сохраняем изменения в базе данных
    db.commit()


def ws_get_user_device_measurements(db: Session, user_id: int, device_id: int):
    '''
    Получение измерений одного устройства полдьзователя
    '''
    user_measurements = get_user_measurements(db=db, user_id=user_id)

    measurements = []
    for measure in user_measurements:
        if measure.device_id == device_id:
            formatted_date = measure.timestamp.strftime('%d.%m.%Y')
            measurements.append({
                "дата": formatted_date,
                "значение": int(measure.value)
            })

    return measurements