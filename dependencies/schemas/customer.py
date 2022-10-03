from typing import Optional
from pydantic import BaseModel

from dependencies.schemas.customer_address import CustomerAddressSchema

class CustomerSchema(BaseModel):
    email: str
    first_name: str
    last_name: str
    customer_address: Optional[CustomerAddressSchema]

    class Config:
        orm_mode = True