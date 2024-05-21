import jwt
from datetime import datetime, timedelta
from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from server.settings import SessionLocal, get_db
import server.schemas as schemas
import server.service as service

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/user/register", summary="Registering a new user")
async def register(user: schemas.UserCreate, db: SessionLocal = Depends(get_db)):
    '''
    Регистрация пользователя
    '''
    db_user = service.get_user_by_username(db, username=user.username)

    if db_user:
        raise HTTPException(status_code=400, detail="User already exist")

    new_user = service.create_user(db=db, user=user)
    return JSONResponse(status_code=201, content={"message": "User created", "data": new_user})

async def authenticate_user(db: SessionLocal, username: str, password: str):
    user = service.get_user_by_username(db, username=username)
    if not user:
        return False
    if not service.verify_password(user.password, password):
        return False
    return user

async def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@app.post("/token", summary="User authorization")
async def login_for_access_token(user: schemas.UserBase, db: SessionLocal = Depends(get_db)):
    '''
    Авторизация
    '''
    db_user = await authenticate_user(db, user.username, user.password)

    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid username or password")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": db_user.username}, expires_delta=access_token_expires
    )

    return JSONResponse(status_code=200, content={"message": "Success", "data": {"access_token": access_token, "token_type": "bearer"}})
async def get_current_user(token: str = Depends(oauth2_scheme)):
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
