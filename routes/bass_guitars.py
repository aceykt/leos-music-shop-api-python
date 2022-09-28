from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import Union

from dependencies.database import get_db

router = APIRouter(
    prefix="/bass-guitars",
    tags=["Bass Guitars"],
    responses={404: {"description" : "Not found"}}
)

@router.get("", status_code=status.HTTP_200_OK)
async def get_all_bass_guitars(db: Session = Depends(get_db)):
    pass

@router.get("/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"id": item_id, "q": q}