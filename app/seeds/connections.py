from app.models import db, environment, SCHEMA, User, Connection

from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_connections():
    # Fetch users from the database
    users = User.query.all()  # Retrieve all users

    for initiator in users:
        for receiver in users:
            if initiator.id != receiver.id:  # Ensure a user does not connect with themselves
                connection = Connection(
                    user_id=initiator.id,
                    connected_id=receiver.id,
                    connection_type='Worked together',  # Example type, adjust as necessary
                    connection_context='On a TV show or movie'  # Example context, adjust as necessary
                )
                db.session.add(connection)

    db.session.commit()  # Commit all connections to the database




# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_connections():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.connections RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM connections"))
        
    db.session.commit()
