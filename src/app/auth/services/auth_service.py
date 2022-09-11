from typing import Any
from jose import JWTError, jwt
from datetime import datetime, timedelta
from src.app.user.models.user_model import User
from src.app.user.schemas.read_user_schema import ReadUserSchema
from src.app.auth.schemas.signin_schema import SigninSchema
from src.app.core.database import get_db
from src.app.core.oauth2_scheme import oauth2_cookie_authorization_scheme, oauth2_header_authorization_scheme
from src.app.core.config import settings
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from src.app.user.services.user_service import user_service
from src.app.helpers.utilities.functions import verify_hash


class AuthService:

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=f"could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    def authenticate_open_api_user(self, *, user_credentials: SigninSchema) -> str:
        try:
            open_api_user = user_service.get_open_api_user(user_credentials=user_credentials)
        except HTTPException as exception:
            if exception.status_code == 404:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST, detail=f"Invalid credentials !"
                )
        token_data = {
            "open_api_user_data": open_api_user
        }
        acess_token = self.create_access_token(data=token_data)
        return {
            "access_token": acess_token,
            **token_data
        }


    def authenticate_user(self, db: Session, *, user_credentials: SigninSchema) -> str:
        try:
            user = user_service.get_one_by_username(db, username=user_credentials.username)
            user_data = {
                key:value 
                for key,value 
                in user.as_dict().items() 
                if key not in [
                    "password", 
                    "profile_picture", 
                    "is_deleted", 
                    "gender", 
                    "user_roles"
                ]
            }
        except HTTPException as exception:
            if exception.status_code == 404:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST, detail=f"Invalid credentials !"
                )
        if not verify_hash(user_credentials.password, user.password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=f"Invalid credentials !"
            )
        token_data = {
            "user_data": user_data,
            "user_roles": [user_role.value for user_role in user.user_roles],
        }
        acess_token = self.create_access_token(data=token_data)
        return {
            "access_token": acess_token,
            **token_data
        }

    def create_access_token(self, *, data: dict) -> str:
        to_encode = data.copy()
        expire_time_in_minutes = datetime.utcnow() + timedelta(
            minutes=settings.JWT_TOKEN_EXPIRE_MINUTES
        )
        to_encode.update({"exp": expire_time_in_minutes})
        jwt_token = jwt.encode(
            to_encode,
            settings.JWT_SECRET_KEY,
            algorithm=settings.JWT_TOKEN_GENERATION_ALGORITHM,
        )
        return jwt_token

    def verify_access_token(self, token: str) -> Any:
        try:
            payload = jwt.decode(
                token,
                settings.JWT_SECRET_KEY,
                algorithms=[settings.JWT_TOKEN_GENERATION_ALGORITHM],
            )
        except JWTError:
            raise self.credentials_exception
        return payload

    def get_current_user(self, db: Session = Depends(get_db), token: str = Depends(oauth2_header_authorization_scheme)) -> ReadUserSchema:
        jwt_token_payload = self.verify_access_token(token)
        try:
            user: User = user_service.get_one_by_id(db, id=jwt_token_payload.get("user_data")["id"])
        except HTTPException:
            raise self.credentials_exception
        return user
    
    def get_current_open_api_user(self, token: str = Depends(oauth2_cookie_authorization_scheme)) -> Any:
        jwt_token_payload = self.verify_access_token(token)
        user_data = jwt_token_payload.get("open_api_user_data")
        user_credentials: SigninSchema = SigninSchema(username=user_data["username"], password=user_data["password"])
        try:
            user: Any = user_service.get_open_api_user(user_credentials=user_credentials)
        except HTTPException:
            raise self.credentials_exception
        return user

auth_service = AuthService()
