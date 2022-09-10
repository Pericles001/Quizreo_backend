from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey

from app.db.init_db import Base


class AnswerOrm(Base):
    """
    Model for answer table
    """
    __tablename__ = "answers"
    id = Column(Integer, primary_key=True)
    content = Column(String(50), unique=True, nullable=False)
    party = Column(Integer, ForeignKey("parties.id"))


class AnswerModel(BaseModel):
    """
    Answer model
    """
    id: int
    content: str
    party: int

    class Config:
        """
        Pydantic config
        """
        orm_mode = True
