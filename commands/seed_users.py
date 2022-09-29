from dependencies.database import SessionLocal
from dependencies.models import Admin, Customer


def seed_users():
    session = SessionLocal()
    
    admins = [
        Admin(id=1, first_name="Leo", last_name="Sanches", email="leonel.sanches@segment.com", password="hackme#123")
    ]

    for admin in admins:
        session.merge(admin)
    session.commit()

    customers = [
        Customer(id=2, first_name="Regular", last_name="Customer", email="regular.customer@segment.com", password="hackme#123")
    ]

    for customer in customers:
        session.merge(customer)
    session.commit()