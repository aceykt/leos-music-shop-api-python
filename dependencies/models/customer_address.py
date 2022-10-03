from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from dependencies.models.base_model import DeclarativeBase

class CustomerAddress(DeclarativeBase):
    __tablename__ = "customer_addresses"

    customer_id = Column(Integer, ForeignKey('customers.customer_id'), primary_key=True)

    address_first_line = Column(String(100), nullable=False)
    address_second_line = Column(String(100), nullable=True)
    city = Column(String(50), nullable=False)
    state = Column(String(50), nullable=False)
    zip_code = Column(Integer, nullable=False)

    customer = relationship(
        'Customer', 
        back_populates='customer_address',
        cascade='all, delete-orphan',
        single_parent=True
    )