from app.models import db, Location, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_locations():
   
   los_angeles = Location(
    city='Los Angeles',
    state='CA',
    country='United States'
    )
   
   atlanta = Location(
        city='Atlanta',
        state='GA',
        country='United States'
    )
   
   new_york = Location(
        city='New York',
        state='NY',
        country='United States'
    )
   
   remote = Location(
        city='Remote',
        state=None,
        country='United States'
    )
   
   db.session.add(los_angeles)
   db.session.add(atlanta)
   db.session.add(new_york)
   db.session.add(remote)
   
   db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_locations():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.locations RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM locations"))
        
    db.session.commit()
