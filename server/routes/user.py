from fastapi import (
    APIRouter,
    HTTPException,
    Depends
)
from werkzeug.security import check_password_hash
from server.settings import SessionLocal
import server.schemas as schemas
import server.service as service

user_router = APIRouter()

DEFAULT_ROUTER = "/user"

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@user_router.post(f"{DEFAULT_ROUTER}/register", response_model=schemas.User)
async def register(user: schemas.UserCreate, db: SessionLocal = Depends(get_db)):
    db_user = service.get_user_by_username(db, username=user.username)

    if db_user:
        raise HTTPException(status_code=400, detail="User already exist")

    return service.create_user(db=db, user=user)

@user_router.post(f"{DEFAULT_ROUTER}/login")
async def login(user: schemas.UserCreate, db: SessionLocal = Depends(get_db)):
    db_user = service.get_user_by_username(db, username=user.username)

    if not db_user:
        raise HTTPException(status_code=401, detail="User doesn't exist")

    if not check_password_hash(db_user.password, user.password):
        raise HTTPException(status_code=403, detail="Password is incorrect")

    return HTTPException(status_code=200, detail="Success")
