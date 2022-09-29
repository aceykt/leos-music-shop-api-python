from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from dependencies.models.base_model import DeclarativeBase

class Order(DeclarativeBase):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"))

    customer = relationship("Customer", back_populates="orders")