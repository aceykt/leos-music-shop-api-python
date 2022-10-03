from typing import Optional
from pydantic import BaseModel

class SignUpSchema(BaseModel):
    email: str
    first_name: str
    last_name: str
    address_first_line: str
    address_second_line: Optional[str]
    city: str
    state: str
    zip_code: int
    password: str