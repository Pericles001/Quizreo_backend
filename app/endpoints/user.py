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


@router.post("/add", response_model=UserModel, status_code=status.HTTP_201_CREATED)
async def create_user(new_user: UserModel, db: Session = Depends(get_db)):
    """
    Method to create new user in database
    :return:
    """
    user = UserOrm(username=new_user.username, firstname=new_user.firstname, lastname=new_user.lastname,
                   email=new_user.email, password=new_user.password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@router.put("/{user_id}", response_model=UserModel, status_code=status.HTTP_200_OK)
async def update_user(user_id: int, edit_user: UserModel, db: Session = Depends(get_db)):
    """
    Method to update user in database
    :return:
    """
    user = db.query(UserOrm).filter(UserOrm.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {user_id} not found")
    user.username = edit_user.username
    user.firstname = edit_user.firstname
    user.lastname = edit_user.lastname
    user.email = edit_user.email
    user.password = edit_user.password
    db.commit()
    db.refresh(user)
    return user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    """
    Deletes a given user from database
    :param user_id:
    :param db:
    :return:
    """
    user = db.query(UserOrm).filter(UserOrm.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User {user_id} not found")
    db.delete(user)
    db.commit()
    return "User deleted"
