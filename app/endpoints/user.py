from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.user import UserModel, UserOrm
from app.database.init_db import get_db

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[UserModel])
async def get_users(db: Session = Depends(get_db)):
    """
    Method that returns all users from database
    :return:
    """
    users = db.query(UserOrm).all()
    return users


@router.get("/{user_id}")
async def get_user():
    """
    Method to get details about a given user
    :return:
    """


@router.post("/add")
async def create_user():
    """
    Method to create new user in database
    :return:
    """


@router.put("/update")
async def update_user():
    """
    Method to update user in database
    :return:
    """


@router.delete("/{user_id}/delete")
async def delete_user():
    """
    Method that delete a user from database
    :return:
    """
