from sqlalchemy import Column, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship

from dependencies.models.base_model import DeclarativeBase

class BassGuitar(DeclarativeBase):
    __tablename__ = "bass_guitars"
    id = Column(Integer, primary_key=True, index=True)
    manufacturer_id = Column(Integer, ForeignKey("manufacturers.id"))

    model = Column(String(150), nullable=False, index=True)
    price = Column(Numeric(10, 2, asdecimal=True), nullable=False)
    main_image = Column(String(500), nullable=True)

    manufacturer = relationship("Manufacturer", back_populates="bass_guitars")

    bass_guitar_guest_orders = relationship("GuestOrderBassGuitar", back_populates="bass_guitar")
    bass_guitar_orders = relationship("OrderBassGuitar", back_populates="bass_guitar")