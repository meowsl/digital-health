from sqlalchemy.orm import Session
import server.models as models
import server.schemas as schemas
from fastapi import (
    HTTPException,
    Depends
)
from werkzeug.security import check_password_hash
from datetime import (
    timedelta,
    datetime
)
import jwt
from server.settings import (
    SECRET_KEY,
    ALGORITHM,
    auth_scheme
)

def get_user(db: Session, user_id: int):
    '''
    Получение пользователя по ID
    '''
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    '''
    Получение пользователя по логину
    '''
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    '''
    Создание нового пользователя
    '''
    db_user = models.User(username=user.username, email=user.email, role=user.role, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user(db: Session, user: schemas.UserBase):
    '''
    Вспомогательная аутентификаци
    '''
    db_user = get_user_by_username(db=db, username=user.username)

    if not db_user:
        return False
        # raise HTTPException(status_code=401, detail="User doesnt exist")

    if not check_password_hash(db_user.password, user.password):
        return False
        # raise HTTPException(status_code=401, detail="Incorrect password")

    return db_user

async def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(auth_scheme)):
    '''
    Получение текущего пользователя
    '''
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except jwt.PyJWTError:
        raise credentials_exception
    user = service.get_user_by_username(db, username=username)
    return user