from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

postgres_user = settings.POSTGRES_USER
postgres_password = settings.POSTGRES_PASSWORD
postgres_server = settings.POSTGRES_SERVER
postgres_port = settings.POSTGRES_PORT
postgres_db = settings.POSTGRES_DB

SQLALCHEMY_DATABASE_URL = f"postgresql://{postgres_user}:{postgres_password}@{postgres_server}:{postgres_port}/{postgres_db}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
