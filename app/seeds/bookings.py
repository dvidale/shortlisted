from app.models import db, Booking, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime

# Adds a demo user, you can add other users here if you want
def seed_bookings():
   
    # John
    booking_john_1 = Booking(
        user_id=4,
        shortlist_id=None,
        start_date=datetime(2024, 8, 1),
        end_date=datetime(2024, 8, 21),
    )

    booking_john_2 = Booking(
        user_id=4,
        shortlist_id=None,
        start_date=datetime(2024, 9, 1),
        end_date=datetime(2024, 11, 1),
    )

    # Jane
    booking_jane_1 = Booking(
        user_id=5,
        shortlist_id=None,
        start_date=datetime(2024, 8, 22),
        end_date=datetime(2024, 9, 12),
    )

    booking_jane_2 = Booking(
        user_id=5,
        shortlist_id=None,
        start_date=datetime(2024, 10, 1),
        end_date=datetime(2024, 12, 1),
    )

    # Michael
    booking_michael_1 = Booking(
        user_id=6,
        shortlist_id=None,
        start_date=datetime(2024, 9, 5),
        end_date=datetime(2024, 9, 26),
    )

    booking_michael_2 = Booking(
        user_id=6,
        shortlist_id=None,
        start_date=datetime(2024, 11, 1),
        end_date=datetime(2025, 1, 1),
    )

    # Emily
    booking_emily_1 = Booking(
        user_id=7,
        shortlist_id=None,
        start_date=datetime(2024, 9, 20),
        end_date=datetime(2024, 10, 10),
    )

    booking_emily_2 = Booking(
        user_id=7,
        shortlist_id=None,
        start_date=datetime(2024, 11, 15),
        end_date=datetime(2025, 1, 15),
    )

    # David
    booking_david_1 = Booking(
        user_id=8,
        shortlist_id=None,
        start_date=datetime(2024, 10, 1),
        end_date=datetime(2024, 10, 21),
    )

    booking_david_2 = Booking(
        user_id=8,
        shortlist_id=None,
        start_date=datetime(2024, 12, 1),
        end_date=datetime(2024, 2, 1),
    )

    # Sarah
    booking_sarah_1 = Booking(
        user_id=9,
        shortlist_id=None,
        start_date=datetime(2024, 10, 15),
        end_date=datetime(2024, 11, 5),
    )

    booking_sarah_2 = Booking(
        user_id=9,
        shortlist_id=None,
        start_date=datetime(2025, 1, 1),
        end_date=datetime(2025, 3, 1),
    )

    # Chris
    booking_chris_1 = Booking(
        user_id=10,
        shortlist_id=None,
        start_date=datetime(2024, 11, 1),
        end_date=datetime(2024, 11, 21),
    )

    booking_chris_2 = Booking(
        user_id=10,
        shortlist_id=None,
        start_date=datetime(2024, 1, 15),
        end_date=datetime(2025, 3, 15),
    )

    # Laura
    booking_laura_1 = Booking(
        user_id=11,
        shortlist_id=None,
        start_date=datetime(2024, 11, 5),
        end_date=datetime(2024, 11, 25),
    )

    booking_laura_2 = Booking(
        user_id=11,
        shortlist_id=None,
        start_date=datetime(2025, 2, 1),
        end_date=datetime(2025, 4, 1),
    )

    # Joshua
    booking_joshua_1 = Booking(
        user_id=12,
        shortlist_id=None,
        start_date=datetime(2024, 11, 20),
        end_date=datetime(2024, 12, 10),
    )

    booking_joshua_2 = Booking(
        user_id=12,
        shortlist_id=None,
        start_date=datetime(2025, 1, 1),
        end_date=datetime(2025, 2, 1),
    )

    # Olivia
    booking_olivia_1 = Booking(
        user_id=13,
        shortlist_id=None,
        start_date=datetime(2024, 12, 5),
        end_date=datetime(2024, 12, 25),
    )

    booking_olivia_2 = Booking(
        user_id=13,
        shortlist_id=None,
        start_date=datetime(2024, 12, 1),
        end_date=datetime(2025, 1, 1),
    )


    db.session.add(booking_john_1)
    db.session.add(booking_john_2)
    db.session.add(booking_jane_1)
    db.session.add(booking_jane_2)
    db.session.add(booking_michael_1)
    db.session.add(booking_michael_2)
    db.session.add(booking_emily_1)
    db.session.add(booking_emily_2)
    db.session.add(booking_david_1)
    db.session.add(booking_david_2)
    db.session.add(booking_sarah_1)
    db.session.add(booking_sarah_2)
    db.session.add(booking_chris_1)
    db.session.add(booking_chris_2)
    db.session.add(booking_laura_1)
    db.session.add(booking_laura_2)
    db.session.add(booking_joshua_1)
    db.session.add(booking_joshua_2)
    db.session.add(booking_olivia_1)
    db.session.add(booking_olivia_2)


    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_bookings():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.bookings RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM bookings"))
        
    db.session.commit()
