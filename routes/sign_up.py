from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import joinedload, Session

from dependencies.database import get_db
from dependencies import models, schemas

router = APIRouter(
    prefix="/sign-up",
    tags=["Users"],
    responses={404: {"description" : "Not found"}}
)

@router.post("")
def do_sign_up(
    request: schemas.SignUpSchema,
    db: Session = Depends(get_db)
):
    customer: models.Customer = models.Customer(
        first_name=request.first_name,
        last_name=request.last_name,
        email=request.email,
        password=request.password
    )

    customer.customer_address = models.CustomerAddress(
        address_first_line=request.address_first_line,
        address_second_line=request.address_second_line,
        city=request.city,
        state=request.state,
        zip_code=request.zip_code
    )
    
    db.add(customer)
    db.commit()
    db.refresh(customer)

    return schemas.UserSchema.from_orm(customer)