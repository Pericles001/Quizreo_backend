from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.database.init_db import get_db
from app.models.quiz import QuizModel, QuizOrm

router = APIRouter(
    prefix="/quizzes",
    tags=["quizzes"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[QuizModel], status_code=status.HTTP_302_FOUND)
async def get_quizzes(db: Session = Depends(get_db)):
    """
    Method that returns all quizzes from database
    :return:
    """
    quizzes = db.query(QuizOrm).all()
    if not quizzes:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No quizzes found")
    return quizzes


@router.get("/{quiz_id}", response_model=QuizModel, status_code=status.HTTP_302_FOUND)
async def get_quiz(quiz_id: int, db: Session = Depends(get_db)):
    """
    Method to get details about a given quiz
    :return:
    """
    quiz = db.query(QuizOrm).filter(QuizOrm.id == quiz_id).first()
    if not quiz:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Quiz {quiz_id} not found")
    return quiz


@router.post("/add", response_model=QuizModel, status_code=status.HTTP_201_CREATED)
async def create_quiz(new_quiz: QuizModel, db: Session = Depends(get_db)):
    """
    Method to create new quiz in database
    :return:
    """
    quiz = QuizOrm(title=new_quiz.title, rate=new_quiz.rate, content=new_quiz.content, answer=new_quiz.answer,
                   user_id=new_quiz.user_id)
    db.add(quiz)
    db.commit()
    db.refresh(quiz)
    return quiz


@router.put("/{quiz_id}", response_model=QuizModel, status_code=status.HTTP_200_OK)
async def update_quiz(quiz_id: int, edit_quiz: QuizModel, db: Session = Depends(get_db)):
    """
    Method to update quiz in database
    :return:
    """
    quiz = db.query(QuizOrm).filter(QuizOrm.id == quiz_id).first()
    if not quiz:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Quiz {quiz_id} not found")
    quiz.title = edit_quiz.title
    quiz.rate = edit_quiz.rate
    quiz.content = edit_quiz.content
    quiz.answer = edit_quiz.answer
    quiz.user_id = edit_quiz.user_id
    db.commit()
    db.refresh(quiz)
    return quiz


@router.delete("/{quiz_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_quiz(quiz_id: int, db: Session = Depends(get_db)):
    """
    Method that delete a quiz from database
    :return:
    """
    quiz = db.query(QuizOrm).filter(QuizOrm.id == quiz_id).first()
    if not quiz:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Quiz {quiz_id} not found")
    db.delete(quiz)
    db.commit()
    return "Quiz deleted"
