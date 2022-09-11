from typing import Any
from fastapi import (
    APIRouter,
    BackgroundTasks,
    Depends
)
from sqlalchemy.orm import Session
from src.app.user.models.user_model import User
from src.app.user.schemas.create_user_shema import CreateUserSchema
from src.app.auth.schemas.signin_schema import SigninSchema
from src.app.user.schemas.read_user_schema import ReadUserSchema
from src.app.auth.schemas.signin_response_schema import SigninResponseSchema
from src.app.user.services.user_service import user_service
from src.app.auth.services.auth_service import auth_service
from src.app.core import database
from src.app.helpers.enums.path_operation_tag_enum import PathOperationTag

router = APIRouter(prefix="/auth", tags=[PathOperationTag.AUTH])

@router.post("/signup", response_model=ReadUserSchema)
def register_user(
    *,
    db: Session = Depends(database.get_db),
    background_tasks: BackgroundTasks,
    createUserSchema: CreateUserSchema
) -> User:
    user = user_service.create(
        db,
        create_user_schema=createUserSchema,
        background_tasks=background_tasks
    )
    return user

@router.post("/signin", response_model=SigninResponseSchema)
def sign_in(
    *,
    user_credentials: SigninSchema,
    db: Session = Depends(database.get_db),
) -> any:
    signin_infos = auth_service.authenticate_user(db, user_credentials=user_credentials)
    sign_in_response = SigninResponseSchema(
        status="successful", 
        access_token=signin_infos["access_token"],
        user_data=signin_infos["user_data"],
        user_roles=signin_infos["user_roles"]
    )
    return sign_in_response

@router.get(
    "/session-status", 
    response_model=Any,
    dependencies=[Depends(auth_service.get_current_user)]
)
def get_session_status() -> Any:
    return { "session_status": "valid" }
