from fastapi import (
    APIRouter,
    HTTPException,
    Depends
)
from fastapi.responses import JSONResponse
from server.settings import (
    SessionLocal,
    get_db
)
import server.schemas as schemas
import server.service as service

devices_router = APIRouter(prefix="/devices", tags=["Devices"])

@devices_router.get("", summary="Get all devices")
async def get_devices(db: SessionLocal = Depends(get_db)):
    '''
    Получение всех устройств
    '''
    return service.get_device_list(db)

@devices_router.post("", summary="Create a new device")
async def post_devices(device: schemas.DeviceBase, db: SessionLocal = Depends(get_db)):
    '''
    Добавление нового устройства
    '''
    device_check = service.get_device_by_name(db, device.name)

    if device_check:
        return HTTPException(status_code=500, detail="Device already exist")


    return service.create_device(db=db, device=device)

@devices_router.get("/{device_id}", summary="Get single device")
async def get_device(device_id: int, db: SessionLocal = Depends(get_db)):
    '''
    Получение одного девайса
    '''
    return service.get_device_by_id(id=device_id, db=db)

@devices_router.get("/user/{user_id}", summary="Get all devices for user")
async def get_devices(user_id: int, db: SessionLocal = Depends(get_db)):
    '''
    Получение устройств определенного пользователя
    '''
    db_user = service.get_user(db, user_id=user_id)

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    return service.get_user_devices(db=db, user_id=user_id)

@devices_router.post("/user/{user_id}", summary="Add new device to user")
async def add_devices(user_id: int, devices: schemas.UserDevices, db: SessionLocal = Depends(get_db)):
    '''
    Добавление устройства для пользователя
    '''
    db_user = service.get_user(db, user_id=user_id)

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    new_user_device = service.add_user_devices(db=db, user_id=user_id, devices=devices)

    return JSONResponse(status_code=200, content={
        "message":"success",
        "data":{
            "user_id": user_id,
            "new_devices": devices.device_id
        }
    })

@devices_router.delete("/user/{user_id}/{device_id}", summary="Delete target device from user")
async def delete_device(user_id: int, device_id: int, db: SessionLocal = Depends(get_db)):
    '''
    Отвязка устройства от пользователя
    '''
    deleted_device = service.delete_user_devices(db=db, user_id=user_id, device_id=device_id)

    if deleted_device:
        return JSONResponse(status_code=200, content={
            "message": "success",
            "data": {
                "user_id": user_id,
                "deleted_device_id": device_id
            }
        })
    else:
        raise HTTPException(status_code=404, detail="Device not found or not associated with the user")