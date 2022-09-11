from typing import List
from fastapi import (
    APIRouter,
    status,
    Depends
)
from src.app.quizreo.models.answer_model import Answer
from src.app.quizreo.schemas.read_answer_schema import ReadAnswerSchema
from src.app.quizreo.services.answer_service import answer_service
from sqlalchemy.orm import Session
from src.app.core import database
from src.app.helpers.enums.path_operation_tag_enum import PathOperationTag

router = APIRouter(prefix="/answers", tags=[PathOperationTag.ANSWERS])

@router.get("/", response_model=List[ReadAnswerSchema])
def get_all(*, db: Session = Depends(database.get_db)) -> List[Answer]:
    return answer_service.get_all(db)


@router.get("/{id}", response_model=ReadAnswerSchema)
def get_one_by_id(*, db: Session = Depends(database.get_db), id: int) -> Answer:
    answer = answer_service.get_one_by_id(db, id=id)
    return answer

@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete(*, db: Session = Depends(database.get_db), id: int):
    return answer_service.soft_delete(db, id=id)
