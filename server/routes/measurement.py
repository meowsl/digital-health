from fastapi import (
    APIRouter,
    HTTPException,
    Depends
)
from server.settings import (
    SessionLocal,
    get_db
)
import server.schemas as schemas
import server.service as service

measurement_routes = APIRouter(prefix="/measurements", tags=["Measurements"])

@measurement_routes.get("", summary="Get all measurements")
async def get_measurements(db: SessionLocal = Depends(get_db)):
    '''
    Получение всех измерений
    '''
    return service.get_all_measurements(db)

@measurement_routes.get("/{user_id}", summary="Get all measurements for user")
async def get_user_measurements(user_id: int, db: SessionLocal = Depends(get_db)):
    '''
    Получение измерений для конкретного пользователя
    '''
    return service.get_user_measurements(db, user_id)

@measurement_routes.post("/{user_id}", summary="Add new measurement for user")
async def add_user_measurement(user_id: int, measurement: schemas.MeasurementCreate, db: SessionLocal = Depends(get_db)):
    '''
    Добавление нового измерения для пользователя
    '''
    return service.create_measurement(db=db, user_id=user_id, measurement=measurement)

@measurement_routes.get("/{user_id}/{device_id}", summary="Get measurements of a specific user device")
async def get_user_device_measurements(user_id: int, device_id: int, db: SessionLocal = Depends(get_db)):
    '''
    Получение измерений определенного устройства для пользователя
    '''
    return service.get_user_device_measurements(db, user_id, device_id)

