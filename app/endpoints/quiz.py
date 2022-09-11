from fastapi import APIRouter

router = APIRouter(
    prefix="/quizzes",
    tags=["quizzes"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_quizzes():
    """
    Method that returns all quizzes from database
    :return:
    """


@router.get("/{quiz_id}")
async def get_quiz():
    """
    Method to get details about a given quiz
    :return:
    """


@router.post("/add")
async def create_quiz():
    """
    Method to create new quiz in database
    :return:
    """


@router.put("/update")
async def update_quiz():
    """
    Method to update quiz in database
    :return:
    """


@router.delete("/{quiz_id}/delete")
async def delete_quiz():
    """
    Method that delete a quiz from database
    :return:
    """
