from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from dependencies.models.base_model import DeclarativeBase

class BassGuitar(DeclarativeBase):
    __tablename__ = "bass_guitars"
    id = Column(Integer, primary_key=True, index=True)
    manufacturer_id = Column(Integer, ForeignKey("manufacturers.id"))

    model = Column(String(150), nullable=False, index=True)

    manufacturer = relationship("Manufacturer", back_populates="bass_guitars")

    bass_guitar_orders = relationship("OrderBassGuitar", back_populates="bass_guitar")