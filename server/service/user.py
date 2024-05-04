from sqlalchemy.orm import Session
import server.models as models
import server.schemas as schemas
from fastapi import HTTPException
from werkzeug.security import check_password_hash

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
        raise HTTPException(status_code=401, detail="User doesnt exist")

    if not check_password_hash(db_user.password, user.password):
        raise HTTPException(status_code=401, detail="Incorrect password")

    return db_user