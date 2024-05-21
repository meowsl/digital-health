from os import getenv
from dotenv import load_dotenv

load_dotenv()

# <-- Main -->
BASE_URL = getenv("BASE_URL")
SECRET_KEY = getenv("SECRET_KEY")
ALGORITHM = getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = getenv("ACCESS_TOKEN_EXPIRE_MINUTES")

# <-- БД -->
DATABASE_FILE = getenv("DATABASE_FILE")
SQLALCHEMY_DATABASE_URL = getenv("SQLALCHEMY_DATABASE_URL")

ORIGINS = [
    "*"
]