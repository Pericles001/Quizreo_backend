from xmlrpc.client import boolean
from fastapi import HTTPException, Depends
from typing import List
from src.app.user.schemas.read_user_schema import ReadUserSchema
from src.app.helpers.utilities.functions import (
    is_any_slice_element_in_list,
    is_slice_in_list,
)
from src.app.auth.services.auth_service import auth_service
from src.app.auth.schemas.token_data_schema import TokenDataSchema


class RoleChecker:
    def __init__(self, allowed_roles: List[str], strict_check: boolean):
        self.allowed_roles = allowed_roles
        self.strict_check = strict_check

    def __call__(
        self, user: ReadUserSchema = Depends(auth_service.get_current_user)
    ):
        user_roles = user.user_types
        if self.strict_check:
            authorised = is_slice_in_list(self.allowed_roles, user_roles)
        else:
            authorised = is_any_slice_element_in_list(
                self.allowed_roles, user_roles
            )
        if not authorised:
            raise HTTPException(status_code=403, detail="Operation not permitted")
