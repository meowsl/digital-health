from fastapi import FastAPI, WebSocket, Depends
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from sqladmin import Admin
from server.settings import (
    ORIGINS,
    Base,
    engine,
    SECRET_KEY,
    BASE_URL,
    get_db,
    SessionLocal
)
from server.routes import (
    devices_router,
    user_router,
    measurement_routes
)
from .admin import *

import server.service as service

db = next(get_db())

app = FastAPI()
auth = AdminAuth(secret_key=SECRET_KEY, db=db)
admin = Admin(app, engine, authentication_backend=auth)

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", include_in_schema=False)
def read_root():
    return RedirectResponse(f"{BASE_URL}/docs")

async def send_message(websocket: WebSocket, message: str):
    await websocket.send_text(message)

async def get_user_devices(websocket: WebSocket, user_id: int, db: SessionLocal):
    devices = ', '.join(service.ws_get_user_devices(db=db, user_id=user_id))
    await send_message(websocket, f"Вот список Ваших устройств: {devices}")

async def generate_measurements(websocket: WebSocket, user_id: int, device_id: int, device_name: str, db: SessionLocal):
    await send_message(websocket, f"Заполнение измерениями запущено. Пожалуйста, ожидайте")
    if device_id == 4:
        service.ws_generate_measurements_steps(db=db, user_id=user_id, device_id=device_id)
    elif device_id == 5:
        service.ws_generate_measurements_pulse(db=db, user_id=user_id, device_id=device_id)
    await send_message(websocket, f"Показатели успешно сохранены! Вызовите функцию '{device_name}' для отображения")

async def get_user_device_measurements(websocket: WebSocket, user_id: int, device_id: int, db: SessionLocal):
    measurements = service.ws_get_user_device_measurements(db=db, user_id=user_id, device_id=device_id)
    await send_message(websocket, f"Ваши показатели за последние 4 дня: {measurements}")

@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int, db: SessionLocal = Depends(get_db)):
    await websocket.accept()
    username = service.get_user(db=db, user_id=user_id)
    hello_counter = 0
    while True:
        data = await websocket.receive_text()
        if data == "devices":
            await get_user_devices(websocket, user_id, db)
        elif data.lower() == "imitation-steps":
            await generate_measurements(websocket, user_id, 4, "Шаги", db)
        elif data.lower() == "imitation-pulse":
            await generate_measurements(websocket, user_id, 5, "Пульс", db)
        elif data.lower() == "steps":
            await get_user_device_measurements(websocket, user_id, 4, db)
        elif data.lower() == "pulse":
            await get_user_device_measurements(websocket, user_id, 5, db)
        elif data.lower() == "привет" and hello_counter < 5:
            hello_counter += 1
            await send_message(websocket, f"Привет, {username}!")
        elif data.lower() == "привет" and hello_counter >= 5:
            await send_message(websocket, "Так появился он... Тайлер Дерден.")
        else:
            hello_counter = 0
            await send_message(websocket, "Необходимо ввести команду")

app.include_router(user_router)
app.include_router(devices_router)
app.include_router(measurement_routes)

admin.add_view(UserAdmin)
admin.add_view(DeviceAdmin)
admin.add_view(DeviceDataAdmin)
admin.add_view(MeasurementAdmin)
