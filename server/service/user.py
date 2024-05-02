from sqlalchemy.orm import Session
import server.models as models
import server.schemas as schemas
from fastapi import HTTPException

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_devices(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    return user.devices

def add_user_devices(db: Session, user_id: int, devices: schemas.UserDevices):
    db_user = get_user(db, user_id=user_id)

    for device_id in devices.device_id:
        device = db.query(models.Device).filter(models.Device.id == device_id).first()
        if not device:
            raise HTTPException(status_code=404, detail="Device not found")

        db_user.devices.append(device)

    db.commit()
    db.refresh(db_user)

    return db_user