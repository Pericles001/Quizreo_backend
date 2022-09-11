from typing import Any, List
from src.app.core.base_schema import ReadModelSchema


class ReadSurveySchema(ReadModelSchema):
   title: str
   content: str
   user_id: int
   user: Any