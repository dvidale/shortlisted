from app.models import db, environment, SCHEMA, User, Location

from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_user_locations():
   
    # Fetch users and locations from the database
   
    los_angeles = Location.query.get(1)
    atlanta = Location.query.get(2)
    new_york = Location.query.get(3)
    remote = Location.query.get(4)

    # Associate locations with users
   # Associate first 40 users with Los Angeles and Remote
    for i in range(1, 41):
        user = User.query.get(i)
        user.locations.append(los_angeles)
        user.locations.append(new_york)
        user.locations.append(remote)

    # Next 30 users with Atlanta and Remote
    for i in range(41, 70):
        user = User.query.get(i)
        user.locations.append(atlanta)
        user.locations.append(remote)


    # Commit the changes to the database
    db.session.commit()



# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_user_locations():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.user_locations RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM user_locations"))
        
    db.session.commit()
