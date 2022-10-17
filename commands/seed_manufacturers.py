from dependencies.database import SessionLocal
from dependencies.models import Manufacturer


def seed_manufacturers():
    session = SessionLocal()
    
    manufacturers = [
        Manufacturer(id=1, name="Fender"),
        Manufacturer(id=2, name="Warwick"),
        Manufacturer(id=3, name="Ibanez"),
        Manufacturer(id=4, name="Squier")
    ]

    for manufacturer in manufacturers:
        session.merge(manufacturer)
    session.commit()