from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from sqladmin import Admin
from .settings import (
    ORIGINS,
    Base,
    engine
)
from .routes import (
    devices_router,
    user_router
)
from .admin import *

app = FastAPI()
admin = Admin(app, engine)

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
    return RedirectResponse("http://localhost:8000/docs")

app.include_router(user_router)
app.include_router(devices_router)

admin.add_view(UserAdmin)
admin.add_view(DeviceAdmin)
admin.add_view(DeviceDataAdmin)