from http.client import HTTPException
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import joinedload, Session

from dependencies.database import get_db
from dependencies import models

router = APIRouter(
    prefix="/bass-guitars",
    tags=["Bass Guitars"],
    responses={404: {"description" : "Not found"}}
)

@router.get("", status_code=status.HTTP_200_OK)
async def get_all_bass_guitars(db: Session = Depends(get_db)):
    bass_guitars = db.query(models.BassGuitar).all()
    return bass_guitars

@router.get("/{id}")
def read_item(id: int, db: Session = Depends(get_db)):
    bass_guitar = db.query(models.BassGuitar) \
        .options(joinedload(models.BassGuitar.manufacturer)) \
        .filter(models.BassGuitar.id == id) \
        .one_or_none()

    if bass_guitar is None:
        raise HTTPException(status_code=404, detail=f"Bass Guitar with Id {id} not found.")

    return bass_guitar