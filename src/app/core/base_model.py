import pytz
from sqlalchemy import Column, String, DateTime, Integer, Boolean, event
from datetime import datetime
import uuid, secrets, random, inflect
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from src.app.helpers.utilities.functions import get_slug_from

inflect_engine = inflect.engine()

@as_declarative()
class BaseModel:
    id = Column(Integer, primary_key=True, nullable=False)
    __name__: str
    created_at = Column(
        DateTime(timezone=True),
        default=datetime.now(pytz.timezone("Africa/Porto-Novo")),
    )
    is_deleted = Column(Boolean, default=False)

    def as_dict(self):
       return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}

    @property
    def slug(self):
        string = f"quizreo{self.created_at}"
        return get_slug_from(string)

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(self) -> str:
        model_name = self.__name__
        model_name = "".join(model_name).lower()
        return inflect_engine.plural(model_name)
