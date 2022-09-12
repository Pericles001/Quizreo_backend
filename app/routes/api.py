from fastapi import APIRouter

from app.endpoints import answer, party, quiz, survey, trial, user

# from app.endpoints import answer, party, quiz, survey, trial, user
router = APIRouter()

router.include_router(answer.router)
router.include_router(party.router)
router.include_router(quiz.router)
router.include_router(survey.router)
router.include_router(trial.router)
router.include_router(user.router)
