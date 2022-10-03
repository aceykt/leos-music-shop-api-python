from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from dependencies import models, schemas
from dependencies.authentication import jwt_methods
from dependencies.database import get_db
from dependencies.segment import analytics_instance


router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
    responses={404: {"description" : "Not found"}}
)


@router.post("", status_code=status.HTTP_202_ACCEPTED)
async def authentication(body: schemas.AuthSchema, db: Session = Depends(get_db)):
    login = body.login
    password = body.password

    user: models.User = db.query(models.User) \
        .filter(models.User.email == login) \
        .one_or_none()

    if user is None:
        raise HTTPException(401, "Not authenticated")

    if not user.verify_password(password):
        raise HTTPException(401, "Not authenticated")

    jwt_token_payload = jwt_methods.sign_jwt(str(user.id))

    analytics_instance.identify(user.id, schemas.UserSchema.from_orm(user).__dict__)

    return jwt_token_payload