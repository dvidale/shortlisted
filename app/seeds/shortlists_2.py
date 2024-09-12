from app.models import db, Shortlist, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime

# Adds a demo user, you can add other users here if you want
def seed_shortlists_2():
# Create the Shortlist record using db.func.now() for timestamps
    

    shortlist_3 = Shortlist(
    title="LA Unscripted Comedy Editors",
    description="Looking for cutters for shows like 'Is It Cake' and 'Are You Smarter Than a 5th Grader'.",
    job_title_id=1,  # Assuming '1' corresponds to 'Editor'
    industry_area_id=2,  # Assuming '2' corresponds to 'Unscripted'
    genre_id=2,  # Assuming '2' corresponds to 'Comedy'
    location_id=1,  # Assuming '1' corresponds to 'Los Angeles, CA'
    start_date=datetime(2024, 10, 5),
    end_date=None,
    optional_img=None,
    created_by_id=1,  # User ID 1 as the creator
    createdAt=db.func.now(),
    updatedAt=db.func.now()
    )

    shortlist_4 = Shortlist(
        title="AEs Anywhere with a Strong Stomach",
        description="Fear Factor style unscripted program slated to ramp up this fall and carry on into the spring. Must have  bowels of steel.",
        job_title_id=2,
        industry_area_id=2,
        genre_id=3,
        location_id=4,
        start_date=datetime(2024, 9, 1),
        end_date=datetime(2025, 5, 5),
        optional_img=None,
        created_by_id=1,
        createdAt=db.func.now(),
        updatedAt=db.func.now()
    )

    # Add to the session and commit
    db.session.add_all([shortlist_3, shortlist_4])


    
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_shortlists_2():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.shortlists RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM shortlists"))
        
    db.session.commit()
