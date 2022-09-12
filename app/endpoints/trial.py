from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.database.init_db import get_db
from app.models.trial import TrialModel, TrialOrm

router = APIRouter(
    prefix="/trials",
    tags=["trials"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[TrialModel], status_code=status.HTTP_302_FOUND)
async def get_trials(db: Session = Depends(get_db)):
    """
    Method that returns all trials from database
    :return:
    """
    trials = db.query(TrialOrm).all()
    if not trials:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No trials found")
    return trials


@router.get("/{trial_id}", response_model=TrialModel, status_code=status.HTTP_302_FOUND)
async def get_trial(trial_id: int, db: Session = Depends(get_db)):
    """
    Method to get details about a given trial
    :return:
    """
    trial = db.query(TrialOrm).filter(TrialOrm.id == trial_id).first()
    if not trial:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Trial {trial_id} not found")
    return trial


@router.post("/add", response_model=TrialModel, status_code=status.HTTP_201_CREATED)
async def create_trial(new_trial: TrialModel, db: Session = Depends(get_db)):
    """
    Method to create new trial in database
    :return:
    """
    trial = TrialOrm(title=new_trial.title, type=new_trial.type, time=new_trial.time, settings=new_trial.settings,
                     quiz=new_trial.quiz, survey=new_trial.survey, user_id=new_trial.user_id)
    db.add(trial)
    db.commit()
    db.refresh(trial)
    return trial


@router.put("/{trial_id}", response_model=TrialModel, status_code=status.HTTP_200_OK)
async def update_trial(trial_id: int, edit_trial: TrialModel, db: Session = Depends(get_db)):
    """
    Method to update trial in database
    :return:
    """
    trial = db.query(TrialOrm).filter(TrialOrm.id == trial_id).first()
    if not trial:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Trial {trial_id} not found")
    trial.title = edit_trial.title
    trial.type = edit_trial.type
    trial.time = edit_trial.time
    trial.settings = edit_trial.settings
    trial.quiz = edit_trial.quiz
    trial.survey = edit_trial.survey
    trial.user_id = edit_trial.user_id
    db.commit()
    db.refresh(trial)
    return trial


@router.delete("/{trial_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_trial(trial_id: int, db: Session = Depends(get_db)):
    """
    Method that delete a trial from database
    :return:
    """
    trial = db.query(TrialOrm).filter(TrialOrm.id == trial_id).first()
    if not trial:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Trial {trial_id} not found")
    db.delete(trial)
    db.commit()
    return "Trial deleted"
