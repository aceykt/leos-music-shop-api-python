from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import joinedload, Session

from dependencies.authentication.user_methods import get_admin_user
from dependencies.database import get_db
from dependencies import models, schemas

router = APIRouter(
    prefix="/customers",
    tags=["Customers"],
    responses={404: {"description" : "Not found"}}
)


@router.get(
    "", 
    status_code=status.HTTP_200_OK, 
    response_model_exclude_none=True
)
async def get_all_customers(db: Session = Depends(get_db), user: models.Admin = Depends(get_admin_user)):
    customers = db.query(models.Customer).all()
    return [schemas.CustomerSchema.from_orm(c) for c in customers]


@router.get("/{id}")
def get_one_customer(id: int, db: Session = Depends(get_db), user: models.Admin = Depends(get_admin_user)):
    customer = db.query(models.Customer) \
        .options(joinedload(models.Customer.customer_address)) \
        .filter(models.Customer.customer_id == id) \
        .one_or_none()

    if customer is None:
        raise HTTPException(status_code=404, detail=f"Customer with Id {id} not found.")

    return schemas.CustomerSchema.from_orm(customer)