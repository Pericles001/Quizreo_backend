from typing import List
from src.app.core.base_schema import UpdateModelSchema


class UpdateSurveySchema(UpdateModelSchema):
   title: str | None
   content: str | None
   user_id: int | None