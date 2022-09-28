from dependencies.database import SessionLocal
from dependencies.models import Manufacturer


def seed_manufacturers():
    session = SessionLocal()
    
    manufacturers = [
        Manufacturer(id=1, model="Fender")
    ]

    for manufacturer in manufacturers:
        session.merge(manufacturer)
    session.commit()