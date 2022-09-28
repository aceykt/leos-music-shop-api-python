from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import Union

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