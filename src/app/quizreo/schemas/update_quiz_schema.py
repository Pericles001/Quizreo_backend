from typing import List
from src.app.core.base_schema import UpdateModelSchema


class UpdateQuizSchema(UpdateModelSchema):
   title: str | None
   rate: int | None
   content: str | None
   answer_id: int | None
   user_id: int | None