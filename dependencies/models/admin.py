from sqlalchemy import Column, ForeignKey, Integer
from dependencies.models.user import User

class Admin(User):
    __tablename__ = 'admins'

    admin_id = Column(Integer, ForeignKey('users.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'admin'
    }

    def __init__(self, id=None, first_name=None, last_name=None, email=None, password=None):
        self.admin_id = id
        super().__init__(id, first_name, last_name, email, password)