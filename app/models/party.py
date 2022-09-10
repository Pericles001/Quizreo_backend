from pydantic import BaseModel


class Party(BaseModel):
    """
    Party model
    """
    id: int
    title: str
    user_id: int


class Config:
    """
    Pydantic config
    """
    orm_mode = True
