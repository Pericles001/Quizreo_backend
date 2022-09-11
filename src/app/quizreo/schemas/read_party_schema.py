from typing import Any
from src.app.core.base_schema import ReadModelSchema


class ReadPartySchema(ReadModelSchema):
   title: str
   user_id: int
   user: Any