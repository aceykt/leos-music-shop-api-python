from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from dependencies.models.base_model import DeclarativeBase
from dependencies.models.base_order import BaseOrder

class Order(DeclarativeBase, BaseOrder):
    __tablename__ = "orders"
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))

    customer = relationship("Customer", back_populates="orders")

    order_bass_guitars = relationship("OrderBassGuitar", back_populates="order")