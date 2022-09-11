from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.app.core.base_model import BaseModel


class Answer(BaseModel):
    content = Column(String(50), unique=True, nullable=False)
    party_id = Column(Integer, ForeignKey("parties.id"))
    party = relationship("Party", back_populates="answers", uselist=False)
    quizzes = relationship("Quiz", back_populates="answer")
