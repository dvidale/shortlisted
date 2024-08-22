from app.models import db, user_job_title, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_user_job_titles():
    
    John = user_job_title(
        user_id=4,
        job_title_id=1  # Editor
    )

    John_2 = user_job_title(
        user_id=4,
        job_title_id=2  # Assistant Editor
    )

    Jane = user_job_title(
        user_id=5,
        job_title_id=2  # Assistant Editor
    )

    Jane_2 = user_job_title(
        user_id=5,
        job_title_id=1  # Editor
    )

    Michael = user_job_title(
        user_id=6,
        job_title_id=1  # Editor
    )

    Michael_2 = user_job_title(
        user_id=6,
        job_title_id=2  # Assistant Editor
    )

    Emily = user_job_title(
        user_id=7,
        job_title_id=2  # Assistant Editor
    )

    Emily_2 = user_job_title(
        user_id=7,
        job_title_id=1  # Editor
    )

    David = user_job_title(
        user_id=8,
        job_title_id=1  # Editor
    )

    David_2 = user_job_title(
        user_id=8,
        job_title_id=2  # Assistant Editor
    )

    Sarah = user_job_title(
        user_id=9,
        job_title_id=2  # Assistant Editor
    )

    Chris = user_job_title(
        user_id=10,
        job_title_id=1  # Editor
    )

    Laura = user_job_title(
        user_id=11,
        job_title_id=2  # Assistant Editor
    )

    Joshua = user_job_title(
        user_id=12,
        job_title_id=1  # Editor
    )

    Olivia = user_job_title(
        user_id=13,
        job_title_id=2  # Assistant Editor
    )

    db.session.add(John)
    db.session.add(John_2)
    db.session.add(Jane)
    db.session.add(Jane_2)
    db.session.add(Michael)
    db.session.add(Michael_2)
    db.session.add(Emily)
    db.session.add(Emily_2)
    db.session.add(David)
    db.session.add(David_2)
    db.session.add(Sarah)
    db.session.add(Chris)
    db.session.add(Laura)
    db.session.add(Joshua)
    db.session.add(Olivia)

    
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_user_job_titles():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.job_titles RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM job_titles"))
        
    db.session.commit()
