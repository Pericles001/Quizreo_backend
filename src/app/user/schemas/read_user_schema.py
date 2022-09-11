from datetime import datetime
from typing import List, Any
from src.app.helpers.enums.gender_enum import Gender
from src.app.core.base_schema import ReadModelSchema
from src.app.helpers.enums.user_role_enum import UserRole


class ReadUserSchema(ReadModelSchema):
    id: int
    firstname: str
    lastname: str
    gender: Gender
    email: str
    phone: str
    username: str | None
    user_roles: List[UserRole]
    profile_picture: str | None
    parties: List[Any]
    quizzes: List[Any]
    surveys: List[Any]
    trials: List[Any]
    created_at: datetime
    is_deleted: bool
    slug: str

    class Config:
        orm_mode = True
        use_enum_values = True
