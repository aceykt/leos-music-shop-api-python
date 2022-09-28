from sqlalchemy import Column, Integer, String

from dependencies.models.base_model import DeclarativeBase

class Manufacturer(DeclarativeBase):
    __tablename__ = "manufacturers"
    id = Column(Integer, primary_key=True, index=True)

    model = Column(String(50), nullable=False, index=True)