from typing import List
from src.app.core.base_schema import CreateModelSchema


class CreateTrialSchema(CreateModelSchema):
   title: str
   type: str
   time: int
   settings: str
   quiz_id: int
   survey_id: int
   user_id: int