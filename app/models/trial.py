from pydantic import BaseModel


class Trial(BaseModel):
    """
    Trial model
    """
    id: int
    title: str
    type: str
    time: int
    settings: int
    quiz: int
    survey: int
    user_id: int

    class Config:
        """
        Pydantic config
        """
        orm_mode = True
