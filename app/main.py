from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.routes.api import router as api_router
from app.database.init_db import engine, sessionLocal
from app.models import user, quiz, survey, trial, party, answer

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


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    "Home route"
    return {"message": "Hello World"}
