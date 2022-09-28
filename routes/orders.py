from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import Union

from dependencies.database import get_db

router = APIRouter(
    prefix="/orders",
    tags=["Orders"],
    responses={404: {"description" : "Not found"}}
)

@router.post("")
def place_new_order():
    return {}