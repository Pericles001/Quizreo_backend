from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, text, TIMESTAMP
from app.database.init_db import Base

class PartyOrm(Base):
    """
    Model for party table
    """
    __tablename__ = "parties"
    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


class PartyModel(BaseModel):
    """
    model for party class
    """
    id: int
    title: str
    user_id: int
    created_at: str

    class Config:
        """
        Pydantic config
        """
        orm_mode = True
