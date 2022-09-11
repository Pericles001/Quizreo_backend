from typing import Any, List
from fastapi import HTTPException, status, UploadFile
from src.app.auth.schemas.signin_schema import SigninSchema
from src.app.core.base_service import BaseService
from src.app.helpers.utilities.functions import set_profile_picture
from src.app.user.models.user_model import User
from sqlalchemy.orm import Session
from src.app.core.config import settings
from fastapi.encoders import jsonable_encoder
from src.app.user.schemas.create_user_shema import CreateUserSchema
from src.app.user.schemas.update_user_schema import UpdateUserSchema


class UserService(BaseService[User, CreateUserSchema, UpdateUserSchema]):
    def create(
        self,
        db: Session,
        *,
        create_user_schema: CreateUserSchema
    ) -> User:
        data = jsonable_encoder(create_user_schema)
        profile_picture = data.pop('profile_picture', None)
        new_user = self.model(**data)
        if profile_picture is not None:
            new_user.profile_picture = set_profile_picture(profile_picture)
        db.add(new_user)
        try:
            db.commit()
        except:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"An error occurred. Please go check what went wrong 🙂️",
            )
        db.refresh(new_user)
        return new_user
    
    def set_user_profile_picture(
        self,
        db: Session,
        *,
        user_slug: str,
        profile_picture: UploadFile | str,
    ) -> User:
        user = self.get_one_by_slug(db, slug=user_slug)
        if profile_picture != None:
            user.profile_picture = set_profile_picture(profile_picture)
        db.add(user)
        try:
            db.commit()
        except:
            db.rollback()
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"An error occurred. Please go check what went wrong 🙂️",
            )
        db.refresh(user)
        return user

    def get_one_by_phone(self, db: Session, *, phone: str) -> User:
        user = db.query(self.model).filter(self.model.phone == phone).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with phone number {phone} does not exist 🙂️",
            )
        return user

    def get_one_by_email(self, db: Session, *, email: str) -> User:
        user = db.query(self.model).filter(self.model.email == email).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with email {email} does not exist 🙂️",
            )
        return user

    def get_one_by_username(self, db: Session, *, username: str) -> User:
        user = db.query(self.model).filter(self.model.username == username.strip()).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with username {username} does not exist 🙂️",
            )
        return user

    def get_one_by_slug(self, db: Session, *, slug: str) -> User:
        user = next((item for item in self.get_all(db) if item.slug == slug), None)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with slug {slug} does not exist 🙂️",
            )
        return user

    def get_one_by_id(self, db: Session, *, id: int) -> User:
        user = db.query(self.model).get(id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {id} does not exist 🙂️",
            )
        return user

    def get_all(self, db: Session) -> List[User]:
        return self.get_multi(db)
    

    def get_open_api_user(self, *, user_credentials: SigninSchema) -> Any:
        open_api_user = settings.OPEN_API_USER
        open_api_user_password = settings.OPEN_API_USER_PASSWORD
        if (not user_credentials.username == open_api_user 
            or not user_credentials.password == open_api_user_password):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Open API user not found 🙂️ !",
            )
        else:
            return {
                "username": open_api_user,
                "password": open_api_user_password
            }


    def delete(self, db: Session, id: int):
        user: User = self.get_one_by_id(db, id=id)
        db.delete(user)
        db.commit()


    def soft_delete(self, db: Session, id: int):
        user: User = self.get_one_by_id(db, id=id)
        user.is_deleted = True
        db.add(user)
        db.commit()
        db.refresh(user)


user_service = UserService(User)
