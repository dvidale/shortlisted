from app.models import db, Shortlist, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime

# Adds a demo user, you can add other users here if you want
def seed_shortlists():
  
  # Assuming the IDs are known and correct
    job_title_id = 2  # ID for Assistant Editor
    industry_area_id = 1  # ID for Scripted Television
    genre_id = 1  # ID for Drama
    location_id = 1  # ID for Los Angeles
    created_by_id = 4  # ID for John

# Create the Shortlist record using db.func.now() for timestamps
    shortlist = Shortlist(
        title="LA Assistant Editors for HBO Drama",
        description="HBO is looking for AEs for the second season of a hit drama starting the second week in January",
        job_title_id=job_title_id,
        industry_area_id=industry_area_id,
        genre_id=genre_id,
        location_id=location_id,
        start_date=datetime(2024, 1, 8),
        end_date=datetime(2025, 5, 31),
        optional_img=None,
        created_by_id=created_by_id,
        createdAt=db.func.now(),
        updatedAt=db.func.now()
    )

    # Add to the session and commit
    db.session.add(shortlist)


    
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_shortlists():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.shortlists RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM shortlists"))
        
    db.session.commit()
