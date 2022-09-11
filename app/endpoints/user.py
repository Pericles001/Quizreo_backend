from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_users():
    """
    Method that returns all users from database
    :return:
    """


@router.get("/{user_id}")
async def get_user():
    """
    Method to get details about a given user
    :return:
    """


@router.post("/add")
async def create_user():
    """
    Method to create new user in database
    :return:
    """


@router.put("/update")
async def update_user():
    """
    Method to update user in database
    :return:
    """


@router.delete("/{user_id}/delete")
async def delete_user():
    """
    Method that delete a user from database
    :return:
    """
