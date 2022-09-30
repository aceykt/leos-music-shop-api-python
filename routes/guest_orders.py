from typing import Union
from fastapi import APIRouter, Depends, Header, status, HTTPException
from sqlalchemy.orm import joinedload, Session

from dependencies import models, schemas
from dependencies.authentication import jwt_methods
from dependencies.authentication.user_methods import get_admin_user, get_customer_user
from dependencies.database import get_db

router = APIRouter(
    prefix="/guest-orders",
    tags=["Orders"],
    responses={404: {"description" : "Not found"}}
)


@router.get("", status_code=status.HTTP_200_OK)
async def get_all_guest_orders(db: Session = Depends(get_db), user: models.Admin = Depends(get_admin_user)):
    guest_orders = db.query(models.GuestOrder).all()
    return guest_orders


@router.get("/{id}")
def get_one_guest_order(id: int, db: Session = Depends(get_db), user: models.Admin = Depends(get_admin_user)):
    guest_order = db.query(models.GuestOrder) \
        .options(joinedload(models.GuestOrder.guest_order_bass_guitars) \
            .joinedload(models.GuestOrderBassGuitar.bass_guitar)) \
        .filter(models.GuestOrder.id == id) \
        .one_or_none()

    if guest_order is None:
        raise HTTPException(status_code=404, detail=f"Guest Order with Id {id} not found.")

    return guest_order
