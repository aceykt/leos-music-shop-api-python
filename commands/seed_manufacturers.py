from dependencies.database import SessionLocal
from dependencies.models import Manufacturer


def seed_manufacturers():
    session = SessionLocal()
    
    manufacturers = [
        Manufacturer(id=1, model="Fender"),
        Manufacturer(id=2, model="Warwick"),
        Manufacturer(id=3, model="Ibanez"),
        Manufacturer(id=4, model="Squier")
    ]

    for manufacturer in manufacturers:
        session.merge(manufacturer)
    session.commit()