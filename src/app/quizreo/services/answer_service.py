from typing import List
from fastapi import HTTPException, status
from src.app.core.base_service import BaseService
from src.app.helpers.utilities.functions import update_values
from src.app.quizreo.models.answer_model import Answer
from src.app.quizreo.schemas.create_answer_schema import CreateAnswerSchema
from src.app.quizreo.schemas.update_answer_schema import UpdateAnswerSchema
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder



class AnswerService(BaseService[Answer, CreateAnswerSchema, UpdateAnswerSchema]):
    def create(
        self,
        db: Session,
        *,
        create_answer_schema: CreateAnswerSchema
    ) -> Answer:
        data = jsonable_encoder(create_answer_schema)
        new_answer = self.model(**data)
        db.add(new_answer)
        try:
            db.commit()
        except:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"An error occured",
            )
        db.refresh(new_answer)
        return new_answer

    def get_one_by_id(self, db: Session, *, id: int) -> Answer:
        user = db.query(self.model).get(id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {id} does not exist",
            )
        return user

    def get_all(self, db: Session) -> List[Answer]:
        return self.get_multi(db)


    def update(
        self,
        db: Session,
        *,
        id: int,
        update_answer_schema: UpdateAnswerSchema
    ) -> Answer:
        answer: Answer = self.get_one_by_id(db, id=id)
        data = jsonable_encoder(update_answer_schema)
        answer = update_values(destination=answer, source=data)
        db.add(answer)
        try:
            db.commit()
        except:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"An error occured",
            )
        db.refresh(answer)
        return answer

    def delete(self, db: Session, id: int):
        answer: Answer = self.get_one_by_id(db, id=id)
        db.delete(answer)
        db.commit()


    def soft_delete(self, db: Session, id: int):
        answer: Answer = self.get_one_by_id(db, id=id)
        answer.is_deleted = True
        db.add(answer)
        db.commit()
        db.refresh(answer)


answer_service = AnswerService(Answer)
