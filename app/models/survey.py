from pydantic import BaseModel


class Survey(BaseModel):
    id: int
    title: str
    content: str
    user_id: int

    class Config:
        """
        Pydantic config
        """
        orm_mode = True
