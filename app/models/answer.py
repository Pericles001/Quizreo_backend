from pydantic import BaseModel


class Answer(BaseModel):
    """
    Answer model
    """
    id: int
    content: str
    party: int

    class Config:
        """
        Pydantic config
        """
        orm_mode = True
