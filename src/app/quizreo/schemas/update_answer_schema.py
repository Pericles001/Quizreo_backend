from typing import List
from src.app.core.base_schema import UpdateModelSchema


class UpdateAnswerSchema(UpdateModelSchema):
   content: str | None
   party_id: int | None
