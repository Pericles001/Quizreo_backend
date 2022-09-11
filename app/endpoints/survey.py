from fastapi import APIRouter

router = APIRouter(
    prefix="/surveys",
    tags=["surveys"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_surveys():
    """
    Method that returns all survey from database
    :return:
    """


@router.get("/{survey_id}")
async def get_survey():
    """
    Method to get details about a given survey
    :return:
    """


@router.post("/add")
async def create_survey():
    """
    Method to create new survey in database
    :return:
    """


@router.put("/update")
async def update_survey():
    """
    Method to update survey in database
    :return:
    """


@router.delete("/{survey_id}/delete")
async def delete_survey():
    """
    Method that delete a survey from database
    :return:
    """
