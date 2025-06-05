from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

DB_USER = os.getenv("DB_USER_APP", "root") # Usar diferentes env vars para la app vs el script si es necesario
DB_PASSWORD = os.getenv("DB_PASSWORD_APP", "password")
DB_HOST = os.getenv("DB_HOST_APP", "localhost") # Reverted to localhost, as primary test engine is SQLite
DB_PORT = os.getenv("DB_PORT_APP", "3306")
DB_NAME = os.getenv("DB_NAME_APP", "hogarfamiliar_test")

# Allow overriding the main app database URL via environment variable
# Default to SQLite in-memory if not specified, to facilitate testing (like schema creation)
# For actual MySQL, set DATABASE_URL_APP_MAIN="mysql+pymysql://user:pass@host/db" in environment
# Using pymysql as it's already in requirements.txt and worked better than mysqlclient previously.
DEFAULT_SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL_APP_MAIN", DEFAULT_SQLALCHEMY_DATABASE_URL)

if SQLALCHEMY_DATABASE_URL.startswith("mysql"):
    print(f"Using MySQL database: {SQLALCHEMY_DATABASE_URL.split('@')[-1]}") # Basic redaction for log
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
else:
    print(f"Using SQLite database: {SQLALCHEMY_DATABASE_URL}")
    # For SQLite, connect_args can be useful, e.g., {"check_same_thread": False} for web apps
    connect_args = {"check_same_thread": False} if SQLALCHEMY_DATABASE_URL == "sqlite:///:memory:" or SQLALCHEMY_DATABASE_URL.startswith("sqlite:///") else {}
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=connect_args)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Global engine for reuse if needed, though SessionLocal is preferred for sessions
current_engine = engine

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
