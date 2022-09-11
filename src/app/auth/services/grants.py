from src.app.auth.services.role_checker import RoleChecker
from src.app.helpers.enums.user_role_enum import UserType


create = RoleChecker(allowed_roles=[UserType.ADMIN.value], strict_check=False)
read = RoleChecker(
    allowed_roles=[
        UserType.USAGER.value,
        UserType.ADMIN.value,
        UserType.POLICE.value,
        UserType.ANAT.value,
        UserType.CNSR.value,
    ],
    strict_check=False,
)
update = RoleChecker(allowed_roles=[UserType.ADMIN.value], strict_check=False)
delete = RoleChecker(allowed_roles=[UserType.ADMIN.value], strict_check=False)
