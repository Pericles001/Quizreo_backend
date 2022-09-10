from pydantic import BaseModel


class Quiz(BaseModel):
    """
    Quiz model
    """
    id: int
    rate: int
    title: str
    content: str
    answer: str
    user_id: int

    class Config:
        """
        Pydantic config
        """
        orm_mode = True
