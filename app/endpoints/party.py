from fastapi import APIRouter

router = APIRouter(
    prefix="/parties",
    tags=["parties"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_parties():
    """
    Method that returns all parties from database
    :return:
    """


@router.get("/{party_id}")
async def get_party():
    """
    Method to get details about a given party
    :return:
    """


@router.post("/add")
async def create_party():
    """
    Method to create new party in database
    :return:
    """


@router.put("/update")
async def update_party():
    """
    Method to update party in database
    :return:
    """


@router.delete("{party_id}/delete")
async def delete_party():
    """
    Method that delete a party from database
    :return:
    """
