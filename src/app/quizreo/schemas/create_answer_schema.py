from typing import List
from src.app.core.base_schema import CreateModelSchema


class CreateAnswerSchema(CreateModelSchema):
   content: str
   party_id: int
