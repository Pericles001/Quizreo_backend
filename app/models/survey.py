from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, text, TIMESTAMP

from app.database.init_db import Base


class SurveyOrm(Base):
    """
    model for survey table
    """
    __tablename__ = "surveys"
    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=True, nullable=False)
    content = Column(String(50), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


class SurveyModel(BaseModel):
    id: int
    title: str
    content: str
    user_id: int
    created_at: str

    class Config:
        """
        Pydantic config
        """
        orm_mode = True
