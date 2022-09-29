from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import joinedload, Session

from dependencies import models
from dependencies.authentication.user_methods import get_admin_user
from dependencies.database import get_db

router = APIRouter(
    prefix="/orders",
    tags=["Orders"],
    responses={404: {"description" : "Not found"}}
)


@router.get("", status_code=status.HTTP_200_OK)
async def get_all_orders(db: Session = Depends(get_db), user: models.Admin = Depends(get_admin_user)):
    orders = db.query(models.Order).all()
    return orders


@router.get("/{id}")
def get_one_order(id: int, db: Session = Depends(get_db), user: models.Admin = Depends(get_admin_user)):
    order = db.query(models.Order) \
        .filter(models.Order.id == id) \
        .one_or_none()

    if order is None:
        raise HTTPException(status_code=404, detail=f"Order with Id {id} not found.")

    return order


@router.post("")
def place_new_order():
    return {}