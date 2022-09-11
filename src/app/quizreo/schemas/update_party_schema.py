from typing import List
from src.app.core.base_schema import UpdateModelSchema


class UpdatePartySchema(UpdateModelSchema):
   title: str | None
   user_id: int | None