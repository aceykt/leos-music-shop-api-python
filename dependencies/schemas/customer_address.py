from typing import Optional
from pydantic import BaseModel

class CustomerAddressSchema(BaseModel):
    address_first_line: str
    address_second_line: Optional[str]
    city: str
    state: str
    zip_code: int

    class Config:
        orm_mode = True