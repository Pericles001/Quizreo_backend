from typing import List, Optional
from src.app.core.base_schema import ReadModelSchema
from src.app.helpers.enums.user_role_enum import UserType


class TokenDataSchema(ReadModelSchema):
    user_id: str
    user_roles: Optional[List[str]]
