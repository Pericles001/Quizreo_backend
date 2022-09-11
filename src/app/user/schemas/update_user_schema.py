from typing import List
from src.app.core.base_schema import UpdateModelSchema
from src.app.helpers.enums.gender_enum import Gender
from src.app.helpers.enums.user_role_enum import UserRole


class UpdateUserSchema(UpdateModelSchema):
    firstname: str | None
    lastname: str | None
    gender: Gender | None
    email: str | None
    phone: str | None
    username: str | None
    password: str | None
    user_types: List[UserRole] | None
    profile_picture: str | None
