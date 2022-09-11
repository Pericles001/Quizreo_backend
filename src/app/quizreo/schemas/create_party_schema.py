from typing import List
from src.app.core.base_schema import CreateModelSchema


class CreatePartySchema(CreateModelSchema):
   title: str
   user_id: int