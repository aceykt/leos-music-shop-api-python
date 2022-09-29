from typing import Optional
from pydantic import BaseModel


class AuthSchema(BaseModel):
    client: Optional[str]
    token: Optional[str]
    login: str
    password: str