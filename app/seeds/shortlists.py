from app.models import db, Shortlist, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime

# Adds a demo user, you can add other users here if you want
def seed_shortlists():
# Create the Shortlist record using db.func.now() for timestamps
    

    shortlist_1 = Shortlist(
    title="NYC Editors for Indie Documentary",
    description="An independent production company is seeking experienced editors for a feature-length documentary exploring social justice issues in New York City. The project is set to begin filming in early February.",
    job_title_id=2,  # Assuming '2' corresponds to 'Editor'
    industry_area_id=4,  # Assuming '4' corresponds to 'Documentary'
    genre_id=3,  # Assuming '3' corresponds to 'Historical'
    location_id=3,  # Assuming '3' corresponds to 'New York, NY'
    start_date=datetime(2024, 2, 5),
    end_date=datetime(2024, 8, 15),
    optional_img=None,
    created_by_id=1,  # User ID 1 as the creator
    createdAt=db.func.now(),
    updatedAt=db.func.now()
    )

    shortlist_2 = Shortlist(
        title="LA Assistant Editors for HBO Drama",
        description="HBO is looking for AEs for the second season of a hit drama starting the second week in January",
        job_title_id=2,
        industry_area_id=1,
        genre_id=1,
        location_id=1,
        start_date=datetime(2024, 1, 9),
        end_date=datetime(2025, 5, 31),
        optional_img=None,
        created_by_id=1,
        createdAt=db.func.now(),
        updatedAt=db.func.now()
    )

    # Add to the session and commit
    db.session.add_all([shortlist_1, shortlist_2])


    
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
