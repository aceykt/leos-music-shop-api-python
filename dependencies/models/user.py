from sqlalchemy import Column, Integer, String

from dependencies.authentication import pwd_context
from dependencies.models.base_model import DeclarativeBase

class User(DeclarativeBase):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String(100), nullable=False, index=True)
    last_name = Column(String(100), nullable=False, index=True)
    email = Column(String(100), nullable=False, index=True)
    user_type = Column(String(50))
    password_hash = Column(String(128), nullable=False)

    def verify_password(self, plain_password):
        return pwd_context.verify(plain_password, self.password_hash)

    def get_password_hash(self, password):
        self.password_hash = pwd_context.hash(password)

    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': user_type
    }

    def __init__(self, id=None, first_name=None, last_name=None, email=None, password=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

        if password:
            self.get_password_hash(password)