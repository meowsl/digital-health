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