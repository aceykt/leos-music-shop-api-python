from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import joinedload, Session

from dependencies.database import get_db
from dependencies import models

router = APIRouter(
    prefix="/manufacturers",
    tags=["Manufacturers"],
    responses={404: {"description" : "Not found"}}
)


@router.get("", status_code=status.HTTP_200_OK)
async def get_all_manufacturers(db: Session = Depends(get_db)):
    manufacturers = db.query(models.Manufacturer).all()
    return manufacturers


@router.get("/{id}")
def get_one_manufacturer(id: int, db: Session = Depends(get_db)):
    manufacturer = db.query(models.Manufacturer) \
        .options(joinedload(models.Manufacturer.bass_guitars)) \
        .filter(models.Manufacturer.id == id) \
        .one_or_none()

    if manufacturer is None:
        raise HTTPException(status_code=404, detail=f"Manufacturer with Id {id} not found.")

    return manufacturer