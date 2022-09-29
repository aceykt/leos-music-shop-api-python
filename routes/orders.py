from typing import Union
from fastapi import APIRouter, Depends, Header, status, HTTPException
from sqlalchemy.orm import joinedload, Session

from dependencies import models, schemas
from dependencies.authentication import jwt_methods
from dependencies.authentication.user_methods import get_admin_user, get_customer_user
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
def place_new_order(
    # request: schemas.OrderSchema,
    db: Session = Depends(get_db),
    authorization: Union[str, None] = Header(default=None)
):
    customer: models.Customer | None = None
    if authorization:
        token: str | None = jwt_methods.validate_jwt_format(authorization)
        if token is None:
            raise HTTPException(status_code=status.HTTP_417_EXPECTATION_FAILED, detail=f"Invalid authentication header")
        token_data: str = jwt_methods.decode_jwt(token)
        customer: models.Customer = get_customer_user(token_data)

    

    return {'authorization': authorization}