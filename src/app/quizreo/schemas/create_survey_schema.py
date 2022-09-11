from typing import List
from src.app.core.base_schema import CreateModelSchema


class CreateSurveySchema(CreateModelSchema):
   title: str
   content: str
   user_id: int