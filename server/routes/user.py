from fastapi import (
    APIRouter,
    HTTPException,
    Depends
)
from werkzeug.security import check_password_hash
from server.settings import (
    SessionLocal,
    get_db
)
import server.schemas as schemas
import server.service as service

user_router = APIRouter(prefix="/user", tags=["Authentication"])

@user_router.post("/register", summary="Registering a new user")
async def register(user: schemas.UserCreate, db: SessionLocal = Depends(get_db)):
    '''
    Регистрация пользователя
    '''
    db_user = service.get_user_by_username(db, username=user.username)

    if db_user:
        raise HTTPException(status_code=400, detail="User already exist")

    return service.create_user(db=db, user=user)

@user_router.post("/login", summary="User authorization")
async def login(user: schemas.UserBase, db: SessionLocal = Depends(get_db)):
    '''
    Авторизация
    '''
    db_user = service.authenticate_user(db=db, user=user)

    return HTTPException(status_code=200, detail="Success")

@user_router.get("/{user_id}/devices", summary="Get all devices for user")
async def get_devices(user_id: int, db: SessionLocal = Depends(get_db)):
    '''
    Получение устройств определенного пользователя
    '''
    db_user = service.get_user(db, user_id=user_id)

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    return service.get_user_devices(db=db, user_id=user_id)

@user_router.post("/{user_id}/devices", summary="Add new device to user")
async def add_devices(user_id: int, devices: schemas.UserDevices , db: SessionLocal = Depends(get_db)):
    '''
    Добавление устройства для пользователя
    '''
    db_user = service.get_user(db, user_id=user_id)

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    return service.add_user_devices(db=db, user_id=user_id, devices=devices)
