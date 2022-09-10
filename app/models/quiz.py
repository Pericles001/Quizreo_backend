from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey

from app.db.init_db import Base


class QuizOrm(Base):
    """
    model for quiz table
    """
    __tablename__ = "quizzes"
    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=True, nullable=False)
    rate = Column(Integer, unique=True, nullable=False)
    content = Column(String(50), unique=True, nullable=False)
    answer = Column(Integer, ForeignKey("answers.id"))
    user_id = Column(Integer, ForeignKey("users.id"))


class QuizModel(BaseModel):
    """
    Quiz model
    """
    id: int
    rate: int
    title: str
    content: str
    answer: str
    user_id: int

    class Config:
        """
        Pydantic config
        """
        orm_mode = True
