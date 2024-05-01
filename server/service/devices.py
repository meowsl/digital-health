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