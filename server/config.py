from os import getenv
from dotenv import load_dotenv

load_dotenv()

# <-- БД -->
DATABASE_FILE = getenv("DATABASE_FILE")
SQLALCHEMY_DATABASE_URL = getenv("SQLALCHEMY_DATABASE_URL")