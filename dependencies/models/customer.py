from sqlalchemy import Column, ForeignKey, Integer
from dependencies.models.user import User

class Customer(User):
    __tablename__ = 'customers'

    customer_id = Column(Integer, ForeignKey('users.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'customer'
    }