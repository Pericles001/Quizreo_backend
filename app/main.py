from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.database.init_db import engine, sessionLocal, get_db
from app.models import user, quiz, survey, trial, party, answer
from app.routes.api import router as api_router

user.Base.metadata.create_all(bind=engine)
quiz.Base.metadata.create_all(bind=engine)
survey.Base.metadata.create_all(bind=engine)
trial.Base.metadata.create_all(bind=engine)
party.Base.metadata.create_all(bind=engine)
answer.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["http://localhost:8005"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


get_db()

@app.get("/")
async def root():
    "Home route"
    return {"message": "Hello World"}
