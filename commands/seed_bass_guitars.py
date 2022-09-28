from dependencies.database import SessionLocal
from dependencies.models.bass_guitar import BassGuitar


def seed_bass_guitars():
    session = SessionLocal()
    
    bass_guitars = [
        BassGuitar(id=1, model="Fender Jazz 5 String")
    ]

    for bass_guitar in bass_guitars:
        session.merge(bass_guitar)
    session.commit()