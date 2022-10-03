from decimal import Decimal

from dependencies.database import SessionLocal
from dependencies.models.bass_guitar import BassGuitar


def seed_bass_guitars():
    session = SessionLocal()
    
    bass_guitars = [
        BassGuitar(
            id=1, 
            manufacturer_id=1, 
            model="Fender Jazz 5 String", 
            price=Decimal(949)
        ),
        BassGuitar(
            id=2, 
            manufacturer_id=2, 
            model="Warwick Corvette 5 String", 
            price=Decimal(1049),
            main_image="https://img.kytary.com/eshop_ie/velky_v2/na/637509632463700000/fa2968b7/64832364/warwick-rockbass-corvette-multiscale-5-string-solid-black-satin.jpg"
        ),
        BassGuitar(
            id=3, 
            manufacturer_id=3, 
            model="Ibanez K5 Fieldy", 
            price=Decimal(999),
            main_image="https://www.ibanez.com/common/product_artist_file/file/p_region_K5_BKF_1P_08.png"
        ),
        BassGuitar(
            id=4, 
            manufacturer_id=4, 
            model="Squier Affinity Jazz Bass", 
            price=Decimal(309.99),
            main_image="https://www.fmicassets.com/Damroot/LgJpg/10001/0378652505_sqr_ins_frt_1_rr.jpg"
        ),
    ]

    for bass_guitar in bass_guitars:
        session.merge(bass_guitar)
    session.commit()