from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.app.core.base_model import BaseModel
from src.app.user.models.user_model import User
from src.app.quizreo.models.answer_model import Answer


class Quiz(BaseModel):
    title = Column(String(50), unique=True, nullable=False)
    rate = Column(Integer, unique=True, nullable=False)
    content = Column(String(50), unique=True, nullable=False)
    answer_id = Column(Integer, ForeignKey("answers.id"))
    answer = relationship("Answer", back_populates="quizzes", uselist=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="quizzes", uselist=False)
    trials = relationship("Trial", back_populates="quiz")