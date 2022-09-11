from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.app.core.base_model import BaseModel


class Survey(BaseModel):
    title = Column(String(50), unique=True, nullable=False)
    content = Column(String(50), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="surveys", uselist=False)
    trials = relationship("Trial", back_populates="survey")