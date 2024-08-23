from app.models import db, environment, SCHEMA, User, Connection

from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_connections():
    # Fetch users from the database
    john = User.query.get(4)  # Assuming John has user_id=4
    users = User.query.filter(User.id != john.id).all()  # Get all users except John

    # Create connection records
    connections = []
    for user in users:
        connection = Connection(
            user_id=user.id,
            connected_id=john.id,
            connection_type='Worked with',
            connection_context='on two seasons of a production',
            createdAt= db.func.now(),
            updatedAt= db.func.now()
        )
        connections.append(connection)

    # Add and commit all connections to the database
    db.session.add_all(connections)
    db.session.commit()




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
