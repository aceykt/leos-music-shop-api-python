from sqlalchemy import Column, ForeignKey, Integer
from dependencies.models.user import User

class Admin(User):
    __tablename__ = 'admins'

    admin_id = Column(Integer, ForeignKey('users.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'admin'
    }