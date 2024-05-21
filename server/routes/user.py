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
from datetime import timedelta
import server.schemas as schemas
import server.service as service
from server.settings.config import ACCESS_TOKEN_EXPIRE_MINUTES

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

    if not db_user:
        raise HTTPException(status_code=400, detail="Логин или пароль неверны!")

    access_token_expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    access_token = await service.create_access_token(
        data={"sub": db_user.username}, expires_delta=access_token_expires
    )

    return JSONResponse(status_code=200, content={
        "message": "Success",
        "data": {
            "access" : access_token,
            "token_type": "bearer"
            }
        }
    )
