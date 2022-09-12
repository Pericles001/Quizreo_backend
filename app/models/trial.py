from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, text, TIMESTAMP

from app.database.init_db import Base


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
    quiz = Column(Integer, ForeignKey("quizzes.id"))
    survey = Column(Integer, ForeignKey("surveys.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


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
    created_at: str

    class Config:
        """
        Pydantic config
        """
        orm_mode = True
