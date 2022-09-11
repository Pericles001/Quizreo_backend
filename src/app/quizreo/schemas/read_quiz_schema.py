from typing import Any, List
from src.app.core.base_schema import ReadModelSchema


class ReadQuizSchema(ReadModelSchema):
   title: str
   rate: int
   content: str
   answer_id: int
   answer: Any
   user_id: int
   usre: Any