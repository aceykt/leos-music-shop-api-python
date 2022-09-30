from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import relationship

from dependencies.models.base_model import DeclarativeBase

class OrderBassGuitar(DeclarativeBase):
    __tablename__ = "orders_bass_guitars"
    id = Column(Integer, primary_key=True, index=True)
    bass_guitar_id = Column(Integer, ForeignKey("bass_guitars.id"))
    order_id = Column(Integer, ForeignKey("orders.id"))

    quantity = Column(Integer, nullable=False)
    historical_price = Column(Integer, nullable=True)

    __table_args__ = (UniqueConstraint('bass_guitar_id', 'order_id', name='iuq_orders_bass_guitars'),)

    bass_guitar = relationship("BassGuitar", back_populates="bass_guitar_orders")
    order = relationship("Order", back_populates="order_bass_guitars")