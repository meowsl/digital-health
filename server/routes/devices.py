from fastapi import APIRouter

devices_router = APIRouter()

DEFAULT_ROUTER = "/devices"

@devices_router.get(f"{DEFAULT_ROUTER}")
def get_devices():
    return {
        "status":"success",
        "data": "list"
    }

@devices_router.post(f"{DEFAULT_ROUTER}")
def post_devices():
    return {
        "status":"success",
        "data":"upload"
    }
