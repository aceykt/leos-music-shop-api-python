from sqlalchemy import Column, Integer, String

from dependencies.models.base_model import DeclarativeBase

class BassGuitar(DeclarativeBase):
    __tablename__ = "bass_guitars"
    id = Column(Integer, primary_key=True, index=True)

    model = Column(String(150), nullable=False, index=True)