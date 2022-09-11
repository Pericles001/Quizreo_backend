from typing import List
from src.app.core.base_schema import CreateModelSchema
from src.app.helpers.enums.gender_enum import Gender
from pydantic import Field
from src.app.helpers.enums.user_role_enum import UserRole


class CreateUserSchema(CreateModelSchema):
    firstname: str
    lastname: str
    gender: Gender
    email: str
    phone: str
    username: str | None
    password: str | None
    user_roles: List[UserRole]
    profile_picture: str | None = Field(
        default=None, 
        title="Optional profile picture of the user"
    )
