from fastapi import FastAPI, Depends
# Create the tables in the database
from sqlalchemy.orm import Session

from app.db.init_db import sessionLocal, engine
from app.models import user, quiz, survey, trial, party, answer

user.Base.metadata.create_all(bind=engine)
quiz.Base.metadata.create_all(bind=engine)
survey.Base.metadata.create_all(bind=engine)
trial.Base.metadata.create_all(bind=engine)
party.Base.metadata.create_all(bind=engine)
answer.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
