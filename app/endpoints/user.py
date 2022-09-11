from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.database.init_db import get_db
from app.models.user import UserModel, UserOrm

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[UserModel], status_code=status.HTTP_302_FOUND)
async def get_users(db: Session = Depends(get_db)):
    """
    Method that returns all users from database
    :return:
    """
    users = db.query(UserOrm).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found")
    return users


@router.get("/{user_id}", response_model=UserModel, status_code=status.HTTP_302_FOUND)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    Method to get details about a given user
    :return:
    """
    user = db.query(UserOrm).filter(UserOrm.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {user_id} not found")
    return user


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
