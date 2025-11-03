import os
from dotenv import load_dotenv
from pathlib import Path

basedir = Path(__file__).resolve().parents[1]
load_dotenv(basedir / ".env")

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        f"sqlite:///{basedir / 'bookbridge.db'}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt-secret-string")
    PROPAGATE_EXCEPTIONS = True

