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

user_router = APIRouter(prefix="/user", tags=["Authorizaton"])

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
async def login(user: schemas.UserCreate, db: SessionLocal = Depends(get_db)):
    '''
    Авторизация
    '''
    db_user = service.get_user_by_username(db, username=user.username)

    if not db_user:
        raise HTTPException(status_code=401, detail="User doesn't exist")

    if not check_password_hash(db_user.password, user.password):
        raise HTTPException(status_code=403, detail="Password is incorrect")

    return HTTPException(status_code=200, detail="Success")
