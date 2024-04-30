from os import getenv, getcwd, sep
import shutil
import dotenv, string, random

class EnvGenerator:

    def __init__(self):
        self.dotenv_path = f"{getcwd()}/.env.example"
        self.new_dotenv_path = f"{getcwd()}/.env"

    def generate_password(self, length, chars=string.ascii_letters + string.digits):
        return "".join(random.choice(chars) for _ in range(length))

    def create_env(self):
        shutil.copy(self.dotenv_path, self.new_dotenv_path)

        dotenv.load_dotenv(self.new_dotenv_path)

        db_file = getenv("DATABASE_FILE")
        dotenv.set_key(self.new_dotenv_path, "SQLALCHEMY_DATABASE_URL", f"sqlite:///{getcwd().replace(sep, '/')}/private/{db_file}")

if __name__ == "__main__":
    generator = EnvGenerator()
    generator.create_env()