from sqlalchemy.orm import Session
import server.models as models
import server.schemas as schemas

def get_device_list(db: Session):
    '''
    Получение списка всех устройств
    '''
    return db.query(models.Device).all()

def get_device_by_name(db: Session, name: str):
    '''
    Получение устройства по названию
    '''
    return db.query(models.Device).filter(models.Device.name == name).first()

def create_device(db: Session, device: schemas.DeviceBase):
    '''
    Создание нового устройства
    '''
    new_device = models.Device(name=device.name)
    for data in device.data:
        new_data = models.DeviceData(indicator=data.indicator, unit=data.unit, device=new_device)
        new_device.data.append(new_data)
    db.add(new_device)
    db.commit()
    db.refresh(new_device)
    return new_device

def get_user_devices(db: Session, user_id: int):
    '''
    Получение всех устройств пользователя
    '''
    user = db.query(models.User).filter(models.User.id == user_id).first()
    return user.devices

def add_user_devices(db: Session, user_id: int, devices: schemas.UserDevices):
    '''
    Добавление нового устройства для пользователя
    '''
    db_user = get_user(db, user_id=user_id)

    for device_id in devices.device_id:
        device = db.query(models.Device).filter(models.Device.id == device_id).first()
        if not device:
            raise HTTPException(status_code=404, detail="Device not found")

        db_user.devices.append(device)

    db.commit()
    db.refresh(db_user)

    return db_user