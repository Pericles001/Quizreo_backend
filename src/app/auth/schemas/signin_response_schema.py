from typing import Any, List
from src.app.core.base_schema import ReadModelSchema


class SigninResponseSchema(ReadModelSchema):
    status: str = "successful"
    access_token: str
    user_data: Any
    user_roles: List[str]
    type: str = "Bearer"
