from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.database.init_db import get_db
from app.models.survey import SurveyModel, SurveyOrm

router = APIRouter(
    prefix="/surveys",
    tags=["surveys"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[SurveyModel], status_code=status.HTTP_302_FOUND)
async def get_surveys(db: Session = Depends(get_db)):
    """
    Method that returns all survey from database
    :return:
    """
    surveys = db.query(SurveyOrm).all()
    if not surveys:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No surveys found")
    return surveys


@router.get("/{survey_id}", response_model=SurveyModel, status_code=status.HTTP_302_FOUND)
async def get_survey(survey_id: int, db: Session = Depends(get_db)):
    """
    Method to get details about a given survey
    :return:
    """
    survey = db.query(SurveyOrm).filter(SurveyOrm.id == survey_id).first()
    if not survey:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Survey {survey_id} not found")
    return survey


@router.post("/add", response_model=SurveyModel, status_code=status.HTTP_201_CREATED)
async def create_survey(new_survey: SurveyModel, db: Session = Depends(get_db)):
    """
    Method to create new survey in database
    :return:
    """
    survey = SurveyOrm(title=new_survey.title, content=new_survey.content, user_id=new_survey.user_id)
    db.add(survey)
    db.commit()
    db.refresh(survey)
    return survey


@router.put("/{survey_id}", response_model=SurveyModel, status_code=status.HTTP_200_OK)
async def update_survey(survey_id: int, edit_survey: SurveyModel, db: Session = Depends(get_db)):
    """
    Method to update survey in database
    :return:
    """
    survey = db.query(SurveyOrm).filter(SurveyOrm.id == survey_id).first()
    if not survey:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Survey {survey_id} not found")
    survey.title = edit_survey.title
    survey.content = edit_survey.content
    survey.user_id = edit_survey.user_id
    db.commit()
    db.refresh(survey)
    return survey


@router.delete("/{survey_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_survey(survey_id: int, db: Session = Depends(get_db)):
    """
    Method that delete a survey from database
    :return:
    """
    survey = db.query(SurveyOrm).filter(SurveyOrm.id == survey_id).first()
    if not survey:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Survey {survey_id} not found")
    db.delete(survey)
    db.commit()
    return "Survey deleted"
