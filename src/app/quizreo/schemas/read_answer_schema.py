from typing import Any
from src.app.core.base_schema import CreateModelSchema, ReadModelSchema


class ReadAnswerSchema(ReadModelSchema):
   content: str
   party_id: int
   party: Any
