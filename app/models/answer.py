from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, text, TIMESTAMP

from app.database.init_db import Base


class AnswerOrm(Base):
    """
    Model for answer table
    """
    __tablename__ = "answers"
    id = Column(Integer, primary_key=True)
    content = Column(String(50), unique=True, nullable=False)
    party = Column(Integer, ForeignKey("parties.id"))
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


class AnswerModel(BaseModel):
    """
    Answer model
    """
    id: int
    content: str
    party: int
    created_at: str

    class Config:
        """
        Pydantic config
        """
        orm_mode = True
