from typing import Optional
from pydantic import BaseModel


class BassGuitarSchema(BaseModel):
    bass_guitar_id: int
    quantity: int