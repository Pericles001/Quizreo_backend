from fastapi import APIRouter

router = APIRouter(
    prefix="/answers",
    tags=["answers"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_answers():
    """
    Method that returns all answers from database
    :return:
    """


@router.get("/{answer_id}")
async def get_answer():
    """
    Method to get details about a given answer
    :return:
    """


@router.post("/add")
async def create_answer():
    """
    Method to create new answer in database
    :return:
    """


@router.put("/update")
async def update_answer():
    """
    Method to update answer in database
    :return:
    """


@router.delete("{answer_id}/delete")
async def delete_answer():
    """
    Method that delete a user from database
    :return:
    """
