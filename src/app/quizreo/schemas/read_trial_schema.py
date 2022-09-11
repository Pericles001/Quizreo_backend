from typing import Any
from src.app.core.base_schema import ReadModelSchema


class ReadTrialSchema(ReadModelSchema):
   title: str
   type: str
   time: int
   settings: str
   quiz_id: int
   quiz: Any
   survey_id: int
   survey: Any
   user_id: int
   user: Any