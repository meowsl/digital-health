from sqlalchemy.orm import Session
import server.models as models
import server.schemas as schemas

def get_all_measurements(db: Session):
    '''
    Получение измерений всех пользователей
    '''
    return db.query(models.Measurement).all()

def get_user_measurements(db: Session, user_id: int):
    '''
    Получение всех измерений пользователя
    '''
    return db.query(models.Measurement).filter(models.Measurement.user_id == user_id).all()

def get_user_device_measurements(db: Session, user_id: int, device_id: int):
    '''
    Получение измерений одного устройства полдьзователя
    '''
    user_measurements = get_user_measurements(db, user_id)

    return [measure for measure in user_measurements if measure.device_id == device_id]

def create_measurement(db: Session, measurement: schemas.MeasurementCreate):
    '''
    Добавление измерения для устройства пользователя
    '''
    new_measurement = models.Measurement(
        user_id=measurement.user_id,
        device_id=measurement.device_id,
        data_id=measurement.data_id,
        value=measurement.value,
        timestamp=measurement.timestamp
    )
    db.add(new_measurement)
    db.commit()
    db.refresh(new_measurement)
    return new_measurement
