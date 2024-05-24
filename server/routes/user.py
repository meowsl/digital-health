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

@user_router.post("/register", summary="Register a new user")
async def register(user: schemas.UserCreate, db: SessionLocal = Depends(get_db)):
    '''
    Регистрация пользователя
    '''
    db_user_username = service.get_user_by_username(db, username=user.username)
    db_user_email = service.get_user_by_email(db, email=user.email)

    if db_user_username:
        raise HTTPException(status_code=400, detail="Пользователь с таким логином уже существует!")

    if db_user_email:
        raise HTTPException(status_code=400, detail="Пользователь с такой почтой уже существует!")

    new_user = service.create_user(db=db, user=user)

    return JSONResponse(status_code=200, content={
        "message":"Success",
        "data": {
            "id": new_user.id,
            "username": user.username,
            "email": user.email
        }
    })

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

    user_info = service.get_user_by_username(username=user.username, db=db)

    user_dict = user_info.__dict__
    del user_dict['_sa_instance_state']
    del user_dict['password']

    return JSONResponse(status_code=200, content={
        "message": "Success",
        "data": {
            "access" : access_token,
            "token_type": "Bearer",
            "user_id": user_dict["id"]
            }
        }
    )

@user_router.get("/{user_id}", summary="Get user information")
async def index(user_id: str, db: SessionLocal = Depends(get_db)):
    '''
    Информация о пользователе
    '''
    db_user = service.get_user(user_id=user_id, db=db)

    user_public = schemas.UserPublic.from_orm(db_user)

    return user_public