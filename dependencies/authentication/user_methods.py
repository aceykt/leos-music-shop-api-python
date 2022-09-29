import logging

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from dependencies import models
from dependencies.authentication import jwt_methods
from dependencies.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
logger = logging.getLogger("jwt_methods")
logger.setLevel(logging.DEBUG)

def get_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        token_id = int(jwt_methods.decode_jwt(token))
        user = db.query(models.User) \
            .filter(models.User.id == token_id) \
            .one_or_none()

        if user is not None:
            return user

        raise HTTPException(status_code=401, detail="Not authenticated")
    except Exception as e:
        logger.debug(e)
        raise e