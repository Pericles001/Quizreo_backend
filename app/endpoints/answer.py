from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.database.init_db import get_db
from app.models.answer import AnswerModel, AnswerOrm

router = APIRouter(
    prefix="/answers",
    tags=["answers"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[AnswerModel], status_code=status.HTTP_302_FOUND)
async def get_answers(db: Session = Depends(get_db)):
    """
    Method that returns all answers from database
    :return:
    """
    answers = db.query(AnswerOrm).all()
    if not answers:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Answers not founc")
    return answers


@router.get("/{answer_id}", response_model=AnswerModel, status_code=status.HTTP_302_FOUND)
async def get_answer(answer_id: int, db: Session = Depends(get_db)):
    """
    Method to get details about a given answer
    :return:
    """
    answer = db.query(AnswerOrm).filter(AnswerOrm.id == answer_id).first()
    if not answer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Party {answer_id} not found")
    return answer


@router.post("/add", response_model=AnswerModel, status_code=status.HTTP_201_CREATED)
async def create_party(new_answer: AnswerModel, db: Session = Depends(get_db)):
    """
    Method to create new answer in database
    :return:
    """
    answer = AnswerOrm(content=new_answer.content, party=new_answer.party)
    db.add(answer)
    db.commit()
    db.refresh(answer)
    return answer


@router.put("/{answer_id}", response_model=AnswerModel, status_code=status.HTTP_200_OK)
async def update_party(answer_id: int, edit_answer: AnswerModel, db: Session = Depends(get_db)):
    """
    Method to update answer in database
    :return:
    """
    answer = db.query(AnswerOrm).filter(AnswerOrm.id == answer_id).first()
    if not answer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Answer {answer_id} not found")
    answer.content = edit_answer.content
    answer.party = answer.party
    db.commit()
    db.refresh(answer)
    return answer


@router.delete("/{answer_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_answer(answer_id: int, db: Session = Depends(get_db)):
    """
    Method that delete  answer from database
    :return:
    """
    answer = db.query(AnswerOrm).filter(AnswerOrm.id == answer_id).first()
    if not answer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Party {answer_id} not found")
    db.delete(answer)
    db.commit()
    return "Answer deleted"
