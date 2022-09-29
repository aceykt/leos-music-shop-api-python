from typing import Optional
from pydantic import BaseModel

from dependencies.schemas.bass_guitar import BassGuitarSchema
from dependencies.schemas.guest_user_data import GuestUserDataSchema

class OrderSchema(BaseModel):
    guest_user_data: Optional[GuestUserDataSchema]
    bass_guitars: Optional[list[BassGuitarSchema]]