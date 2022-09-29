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

    def verify_password(plain_password, hashed_password):
        return pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(password):
        return pwd_context.hash(password)

    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': user_type
    }