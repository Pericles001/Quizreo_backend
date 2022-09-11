from typing import List
from src.app.core.base_schema import UpdateModelSchema


class UpdateTrialSchema(UpdateModelSchema):
   title: str | None
   type: str | None
   time: int | None
   settings: str | None
   quiz_id: int | None 
   survey_id: int | None
   user_id: int | None