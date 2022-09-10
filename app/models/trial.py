from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey

from app.db.init_db import Base


class TrialOrm(Base):
    """
    model for trial table
    """
    __tablename__ = "trials"
    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=True, nullable=False)
    type = Column(String(50), unique=True, nullable=False)
    time = Column(Integer, unique=True, nullable=False)
    settings = Column(Integer, unique=True, nullable=False)
    quiz = Column(Integer, unique=True, nullable=False, foreign_key="quizzes.id")
    survey = Column(Integer, unique=True, nullable=False, foreign_key="surveys.id")
    user_id = Column(Integer, ForeignKey("users.id"))


class TrialModel(BaseModel):
    """
    Trial model
    """
    id: int
    title: str
    type: str
    time: int
    settings: int
    quiz: int
    survey: int
    user_id: int

    class Config:
        """
        Pydantic config
        """
        orm_mode = True
