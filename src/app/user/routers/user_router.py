from typing import List
from fastapi import (
    APIRouter,
    Depends,
    status
)
from sqlalchemy.orm import Session
from src.app.user.models.user_model import User
from src.app.helpers.enums.path_operation_tag_enum import PathOperationTag
from src.app.user.schemas.read_user_schema import ReadUserSchema
from src.app.user.services.user_service import user_service
from src.app.core import database

router = APIRouter(prefix="/users", tags=[PathOperationTag.USERS])


@router.get("/", response_model=List[ReadUserSchema])
def get_all(*, db: Session = Depends(database.get_db)) -> List[User]:
    return user_service.get_all(db)


@router.get("/{id}", response_model=ReadUserSchema)
def get_one_by_id(*, db: Session = Depends(database.get_db), id: int) -> User:
    user = user_service.get_one_by_id(db, id=id)
    return user

@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete(*, db: Session = Depends(database.get_db), id: int):
    return user_service.soft_delete(db, id=id)
