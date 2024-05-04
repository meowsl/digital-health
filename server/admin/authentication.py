from sqladmin.authentication import AuthenticationBackend
from fastapi.requests import Request
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware import Middleware
from server.models import User
from server.service import (
    authenticate_user,
    get_user
)
from server.schemas import UserBase
from server.settings import (
    SessionLocal,
    SECRET_KEY
)

class AdminAuth(AuthenticationBackend):
    '''
    Авторизация в админ панеле
    '''

    def __init__(self, secret_key: str, db: SessionLocal):
        self.db = db
        self.secret_key = secret_key
        self.middlewares = [
            Middleware(SessionMiddleware, secret_key=SECRET_KEY),
        ]

    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = form["username"], form["password"]

        form_data = {
            "username":username,
            "password":password
        }

        user = UserBase(**form_data)

        user = authenticate_user(self.db, user)
        if user and user.role == 'admin':
            request.session.update({"token": "...", "user_id": user.id, "role": user.role})
            return True
        else:
            return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")

        if not token:
            return False

        user_id = request.session.get("user_id")
        role = request.session.get("role")
        if user_id and role == 'admin':
            user = get_user(db=self.db, user_id=user_id)
            if user and user.role == 'admin':
                return True

        return False