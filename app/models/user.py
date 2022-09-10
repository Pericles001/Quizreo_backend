from pydantic import BaseModel


class User(BaseModel):
    """
    User model
    """
    id: int
    username: str
    firstname: str
    lastname: str
    email: str
    password: str

    class Config:
        """
        Pydantic config
        """
        orm_mode = True


class UserInDB(User):
    """
    User model with hashed password
    """
    hashed_password: str
