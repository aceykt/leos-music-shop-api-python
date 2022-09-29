from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from dependencies.models.user import User

class Customer(User):
    __tablename__ = 'customers'

    customer_id = Column(Integer, ForeignKey('users.id'), primary_key=True)

    orders = relationship("Order", back_populates="customer")

    __mapper_args__ = {
        'polymorphic_identity': 'customer'
    }

    def __init__(self, id=None, first_name=None, last_name=None, email=None, password=None):
        self.customer_id = id
        super().__init__(id, first_name, last_name, email, password)