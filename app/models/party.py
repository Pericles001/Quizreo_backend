from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey

from app.db.init_db import Base


class PartyOrm(Base):
    """
    Model for party table
    """
    __tablename__ = "parties"
    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))


class PartyModel(BaseModel):
    """
    model for party class
    """
    id: int
    title: str
    user_id: int

    class Config:
        """
        Pydantic config
        """
        orm_mode = True
