from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from sqladmin import Admin
from server.settings import (
    ORIGINS,
    Base,
    engine,
    SECRET_KEY,
    BASE_URL,
    get_db
)
from server.routes import (
    devices_router,
    user_router,
    measurement_routes
)
from .admin import *

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

app.include_router(user_router)
app.include_router(devices_router)
app.include_router(measurement_routes)

admin.add_view(UserAdmin)
admin.add_view(DeviceAdmin)
admin.add_view(DeviceDataAdmin)
admin.add_view(MeasurementAdmin)