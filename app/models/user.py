from pydantic import BaseModel
from sqlalchemy import Column, Integer, String

from app.db.init_db import Base


class UserOrm(Base):
    """
    Model for user table
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)


class UserModel(BaseModel):
    """
    User model
    """
    id: int
    username: str
    firstname: str
    lastname: str
    email: str
    password: str

    class Config:
        """
        Pydantic config
        """
        orm_mode = True


class UserInDB(UserModel):
    """
    User model with hashed password
    """
    hashed_password: str
