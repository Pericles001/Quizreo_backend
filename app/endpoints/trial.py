from fastapi import APIRouter

router = APIRouter(
    prefix="/trials",
    tags=["trials"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_trials():
    """
    Method that returns all trials from database
    :return:
    """


@router.get("/{trial_id}")
async def get_trial():
    """
    Method to get details about a given trial
    :return:
    """


@router.post("/add")
async def create_trial():
    """
    Method to create new trial in database
    :return:
    """


@router.put("/update")
async def update_trial():
    """
    Method to update trial in database
    :return:
    """


@router.delete("/{trial_id}/delete")
async def delete_trial():
    """
    Method that delete a trial from database
    :return:
    """
