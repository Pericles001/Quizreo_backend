from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.app.core.base_model import BaseModel


class Trial(BaseModel):
    title = Column(String(50), unique=True, nullable=False)
    type = Column(String(50), unique=True, nullable=False)
    time = Column(Integer, unique=True, nullable=False)
    settings = Column(Integer, unique=True, nullable=False)
    quiz_id = Column(Integer, ForeignKey("quizzes.id"), unique=True, nullable=False)
    quiz = relationship("Quiz", back_populates="trials", uselist=False)
    survey_id = Column(Integer, ForeignKey("surveys.id"), unique=True, nullable=False)
    survey = relationship("Survey", back_populates="trials", uselist=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="trials", uselist=False)
