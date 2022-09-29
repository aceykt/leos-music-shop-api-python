from fastapi import APIRouter, Depends, status
from dependencies.authentication.user_methods import get_user

from dependencies import models, schemas

router = APIRouter(
    prefix="/me",
    tags=["Users"],
    responses={404: {"description" : "Not found"}}
)

@router.get("", status_code=status.HTTP_200_OK)
async def get_my_information(user: models.User = Depends(get_user)):
    return schemas.UserSchema.from_orm(user)