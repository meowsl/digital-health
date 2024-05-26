from fastapi import WebSocket, Depends
from sqlalchemy.orm import Session
from server.settings import get_db
from server.service import (
    ws_get_user_devices,
    ws_generate_measurements_steps,
    ws_generate_measurements_pulse,
    ws_get_user_device_measurements,
    get_user
)
import json

async def send_message(websocket: WebSocket, message: dict):
    await websocket.send_text(json.dumps(message))

async def get_user_devices(websocket: WebSocket, user_id: int, db: Session):
    devices = ', '.join(ws_get_user_devices(db=db, user_id=user_id))
    await send_message(websocket, {"type": "devices", "content": f"Вот список Ваших устройств: {devices}"})

async def generate_measurements(websocket: WebSocket, user_id: int, device_id: int, device_name: str, db: Session):
    await send_message(websocket, {"type": "message", "content": f"Заполнение измерениями запущено. Пожалуйста, ожидайте"})
    if device_id == 4:
        ws_generate_measurements_steps(db=db, user_id=user_id, device_id=device_id)
    elif device_id == 5:
        ws_generate_measurements_pulse(db=db, user_id=user_id, device_id=device_id)
    await send_message(websocket, {"type": "message", "content": f"Показатели успешно сохранены! Вызовите функцию '{device_name}' для отображения"})

async def get_user_device_measurements(websocket: WebSocket, user_id: int, device_id: int, db: Session):
    measurements = ws_get_user_device_measurements(db=db, user_id=user_id, device_id=device_id)
    await send_message(websocket, {"type": "measurements", "content": f"Ваши показатели за последние 4 дня: {measurements}"})

async def websocket_endpoint(websocket: WebSocket, user_id: int, db: Session = Depends(get_db)):
    await websocket.accept()
    username = get_user(db=db, user_id=user_id)
    hello_counter = 0
    while True:
        data = await websocket.receive_text()
        received_message = json.loads(data)
        if received_message["type"] == "message":
            if received_message["content"].lower() == "привет" and hello_counter < 5:
                hello_counter += 1
                await send_message(websocket, {"type": "message", "content": f"Привет, {username}!"})
            elif received_message["content"].lower() == "привет" and hello_counter >= 5:
                await send_message(websocket, {"type": "message", "content": "Так появился он... Тайлер Дерден."})
            else:
                hello_counter = 0
                await send_message(websocket, {"type": "message", "content": "Необходимо ввести команду"})
        elif received_message["type"] == "devices":
            await get_user_devices(websocket, user_id, db)

        elif received_message["type"] == "measurements":
            if received_message["action"] == "get":
                if received_message["data"] == "steps":
                    await get_user_device_measurements(websocket, user_id, 4, db)
                elif received_message["data"] == "pulse":
                    await get_user_device_measurements(websocket, user_id, 5, db)
            elif received_message["action"] == "imitation-steps":
                await generate_measurements(websocket, user_id, 4, "Шаги", db)
            elif received_message["action"] == "imitation-pulse":
                await generate_measurements(websocket, user_id, 5, "Пульс", db)
