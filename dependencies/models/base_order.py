from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from dependencies.models.base_model import DeclarativeBase

class BaseOrder:
    id = Column(Integer, primary_key=True, index=True)
