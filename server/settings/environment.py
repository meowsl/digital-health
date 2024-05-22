import shutil, dotenv, string, secrets, os

class EnvGenerator:

    def __init__(self):
        self.dotenv_path = f"{os.getcwd()}/.env.example"
        self.new_dotenv_path = f"{os.getcwd()}/.env"

    def generate_key(self, length=64):
        chars = string.ascii_letters + string.digits + string.punctuation
        return "".join(secrets.choice(chars) for _ in range(length))

    def create_env(self):
        secret_key = self.generate_key()

        shutil.copy(self.dotenv_path, self.new_dotenv_path)

        dotenv.load_dotenv(self.new_dotenv_path)

        dotenv.set_key(self.new_dotenv_path, "SECRET_KEY", secret_key)

        db_file = os.getenv("DATABASE_FILE")
        db_path = os.path.join(os.getcwd(), "private", db_file)
        db_url = f"sqlite:///{db_path}"
        dotenv.set_key(self.new_dotenv_path, "SQLALCHEMY_DATABASE_URL", db_url)

if __name__ == "__main__":
    generator = EnvGenerator()
    generator.create_env()