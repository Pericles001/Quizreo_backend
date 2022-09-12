from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.database.init_db import get_db
from app.models.party import PartyModel, PartyOrm

router = APIRouter(
    prefix="/parties",
    tags=["parties"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[PartyModel], status_code=status.HTTP_302_FOUND)
async def get_parties(db: Session = Depends(get_db)):
    """
    Method that returns all parties from database
    :return:
    """
    parties = db.query(PartyOrm).all()
    if not parties:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Parties not founc")
    return parties


@router.get("/{party_id}", response_model=PartyModel, status_code=status.HTTP_302_FOUND)
async def get_party(party_id: int, db: Session = Depends(get_db)):
    """
    Method to get details about a given party
    :return:
    """
    party = db.query(PartyOrm).filter(PartyOrm.id == party_id).first()
    if not party:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Party {party_id} not found")
    return party


@router.post("/add", response_model=PartyModel, status_code=status.HTTP_201_CREATED)
async def create_party(new_party: PartyModel, db: Session = Depends(get_db)):
    """
    Method to create new party in database
    :return:
    """
    party = PartyOrm(title=new_party.title, user_id=new_party.user_id)
    db.add(party)
    db.commit()
    db.refresh(party)
    return party


@router.put("/{party_id}", response_model=PartyModel, status_code=status.HTTP_200_OK)
async def update_party(party_id: int, edit_party: PartyModel, db: Session = Depends(get_db)):
    """
    Method to update party in database
    :return:
    """
    party = db.query(PartyOrm).filter(PartyOrm.id == party_id).first()
    if not party:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Party {party_id} not found")
    party.title = edit_party.title
    party.user_id = edit_party.user_id
    db.commit()
    db.refresh(party)
    return party


@router.delete("/{party_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_party(party_id: int, db: Session = Depends(get_db)):
    """
    Method that delete a party from database
    :return:
    """
    party = db.query(PartyOrm).filter(PartyOrm.id == party_id).first()
    if not party:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Party {party_id} not found")
    db.delete(party)
    db.commit()
    return "Party deleted"
