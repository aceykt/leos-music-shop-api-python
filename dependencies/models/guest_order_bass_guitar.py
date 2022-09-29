from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import relationship

from dependencies.models.base_model import DeclarativeBase

class GuestOrderBassGuitar(DeclarativeBase):
    __tablename__ = "guest_orders_bass_guitars"
    id = Column(Integer, primary_key=True, index=True)
    bass_guitar_id = Column(Integer, ForeignKey("bass_guitars.id"))
    guest_order_id = Column(Integer, ForeignKey("guest_orders.id"))

    __table_args__ = (UniqueConstraint('bass_guitar_id', 'guest_order_id', name='iuq_guest_orders_bass_guitars'),)

    bass_guitar = relationship("BassGuitar", back_populates="bass_guitar_guest_orders")
    guest_order = relationship("GuestOrder", back_populates="guest_order_bass_guitars")