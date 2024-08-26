from app.models import db, Booking, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime
import pytz


# Adds a demo user, you can add other users here if you want
def seed_bookings():
    tz = pytz.utc
   # John's bookings
    booking_john_1 = Booking(
        user_id=4,
        shortlist_id=None,
        start_date=datetime(2024, 8, 1, tzinfo=tz),
        end_date=datetime(2024, 8, 21, tzinfo=tz),
    )

    booking_john_2 = Booking(
        user_id=4,
        shortlist_id=None,
        start_date=datetime(2024, 9, 1, tzinfo=tz),
        end_date=datetime(2024, 11, 1, tzinfo=tz),
    )

    # Jane's bookings
    booking_jane_1 = Booking(
        user_id=5,
        shortlist_id=None,
        start_date=datetime(2024, 8, 22, tzinfo=tz),
        end_date=datetime(2024, 9, 12, tzinfo=tz),
    )

    booking_jane_2 = Booking(
        user_id=5,
        shortlist_id=None,
        start_date=datetime(2024, 10, 1, tzinfo=tz),
        end_date=datetime(2024, 12, 1, tzinfo=tz),
    )

    # Michael's bookings
    booking_michael_1 = Booking(
        user_id=6,
        shortlist_id=None,
        start_date=datetime(2024, 9, 5, tzinfo=tz),
        end_date=datetime(2024, 9, 26, tzinfo=tz),
    )

    booking_michael_2 = Booking(
        user_id=6,
        shortlist_id=None,
        start_date=datetime(2024, 11, 1, tzinfo=tz),
        end_date=datetime(2025, 1, 1, tzinfo=tz),
    )

    # Emily's bookings
    booking_emily_1 = Booking(
        user_id=7,
        shortlist_id=None,
        start_date=datetime(2024, 9, 20, tzinfo=tz),
        end_date=datetime(2024, 10, 10, tzinfo=tz),
    )

    booking_emily_2 = Booking(
        user_id=7,
        shortlist_id=None,
        start_date=datetime(2024, 11, 15, tzinfo=tz),
        end_date=datetime(2025, 1, 15, tzinfo=tz),
    )

    # David's bookings
    booking_david_1 = Booking(
        user_id=8,
        shortlist_id=None,
        start_date=datetime(2024, 10, 1, tzinfo=tz),
        end_date=datetime(2024, 10, 21, tzinfo=tz),
    )

    booking_david_2 = Booking(
        user_id=8,
        shortlist_id=None,
        start_date=datetime(2024, 12, 1, tzinfo=tz),
        end_date=datetime(2025, 2, 1, tzinfo=tz),
    )

    # Sarah's bookings
    booking_sarah_1 = Booking(
        user_id=9,
        shortlist_id=None,
        start_date=datetime(2024, 10, 15, tzinfo=tz),
        end_date=datetime(2024, 11, 5, tzinfo=tz),
    )

    booking_sarah_2 = Booking(
        user_id=9,
        shortlist_id=None,
        start_date=datetime(2025, 1, 1, tzinfo=tz),
        end_date=datetime(2025, 3, 1, tzinfo=tz),
    )

    # Chris's bookings
    booking_chris_1 = Booking(
        user_id=10,
        shortlist_id=None,
        start_date=datetime(2024, 11, 1, tzinfo=tz),
        end_date=datetime(2024, 11, 21, tzinfo=tz),
    )

    booking_chris_2 = Booking(
        user_id=10,
        shortlist_id=None,
        start_date=datetime(2025, 1, 15, tzinfo=tz),
        end_date=datetime(2025, 3, 15, tzinfo=tz),
    )

    # Laura's bookings
    booking_laura_1 = Booking(
        user_id=11,
        shortlist_id=None,
        start_date=datetime(2024, 11, 5, tzinfo=tz),
        end_date=datetime(2024, 11, 25, tzinfo=tz),
    )

    booking_laura_2 = Booking(
        user_id=11,
        shortlist_id=None,
        start_date=datetime(2025, 2, 1, tzinfo=tz),
        end_date=datetime(2025, 4, 1, tzinfo=tz),
    )

    # Joshua's bookings
    booking_joshua_1 = Booking(
        user_id=12,
        shortlist_id=None,
        start_date=datetime(2024, 11, 20, tzinfo=tz),
        end_date=datetime(2024, 12, 10, tzinfo=tz),
    )

    booking_joshua_2 = Booking(
        user_id=12,
        shortlist_id=None,
        start_date=datetime(2025, 1, 1, tzinfo=tz),
        end_date=datetime(2025, 2, 1, tzinfo=tz),
    )

    # Olivia's bookings
    booking_olivia_1 = Booking(
        user_id=13,
        shortlist_id=None,
        start_date=datetime(2024, 12, 5, tzinfo=tz),
        end_date=datetime(2024, 12, 25, tzinfo=tz),
    )

    booking_olivia_2 = Booking(
        user_id=13,
        shortlist_id=None,
        start_date=datetime(2024, 12, 1, tzinfo=tz),
        end_date=datetime(2025, 1, 1, tzinfo=tz),
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
