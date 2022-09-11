from typing import List
from src.app.core.base_schema import CreateModelSchema


class CreateQuizSchema(CreateModelSchema):
   title: str
   rate: int
   content: str
   answer_id: int
   user_id: int