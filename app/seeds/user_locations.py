from app.models import db, environment, SCHEMA, User, Location

from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_user_locations():
   
    # Fetch users and locations from the database
    john = User.query.get(4)
    jane = User.query.get(5)
    michael = User.query.get(6)
    emily = User.query.get(7)
    david = User.query.get(8)
    sarah = User.query.get(9)
    chris = User.query.get(10)
    laura = User.query.get(11)
    joshua = User.query.get(12)
    olivia = User.query.get(13)

    los_angeles = Location.query.get(1)
    atlanta = Location.query.get(2)
    new_york = Location.query.get(3)
    remote = Location.query.get(4)

    # Associate locations with users
    john.locations.append(los_angeles)  # John - Los Angeles
    john.locations.append(remote)  # John - Remote

    jane.locations.append(los_angeles)  # Jane - Los Angeles
    jane.locations.append(remote)  # Jane - Remote

    michael.locations.append(los_angeles)  # Michael - Los Angeles
    michael.locations.append(remote)  # Michael - Remote

    emily.locations.append(atlanta)  # Emily - Atlanta
    emily.locations.append(remote)  # Emily - Remote

    david.locations.append(atlanta)  # David - Atlanta
    david.locations.append(remote)  # David - Remote

    sarah.locations.append(new_york)  # Sarah - New York
    sarah.locations.append(remote)  # Sarah - Remote

    chris.locations.append(new_york)  # Chris - New York
    chris.locations.append(remote)  # Chris - Remote

    laura.locations.append(new_york)  # Laura - New York
    laura.locations.append(remote)  # Laura - Remote

    joshua.locations.append(remote)  # Joshua - Remote
    joshua.locations.append(los_angeles)  # Joshua - Los Angeles

    olivia.locations.append(remote)  # Olivia - Remote
    olivia.locations.append(los_angeles)  # Olivia - Los Angeles

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
