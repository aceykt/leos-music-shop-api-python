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
    