from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo', 
        email='demo@aa.io', 
        password='password',
        first_name='demo',
        last_name='user')
    marnie = User(
        username='marnie', 
        email='marnie@aa.io', password='password',
        first_name='marnie',
        last_name='marnie')
    bobbie = User(
        username='bobbie', 
        email='bobbie@aa.io', password='password',
        first_name='bobbie',
        last_name='bobbie')
    John = User(
        username='john.doe@example.com',
        email='john.doe@example.com',
        phone_number='1234567890',
        password='password',
        first_name='John',
        last_name='Doe',
        profile_img_url= 'https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/man-001.jpg' ,
    )

    Jane = User(
        username='jane.smith@example.com',
        email='jane.smith@example.com',
        phone_number='2345678901',
        password='password',
        first_name='Jane',
        last_name='Smith',
    )

    Michael = User(
        username='michael.jones@example.com',
        email='michael.jones@example.com',
        phone_number='3456789012',
        password='password',
        first_name='Michael',
        last_name='Jones',
    )

    Emily = User(
        username='emily.williams@example.com',
        email='emily.williams@example.com',
        phone_number='4567890123',
        password='password',
        first_name='Emily',
        last_name='Williams',
    )

    David = User(
        username='david.brown@example.com',
        email='david.brown@example.com',
        phone_number='5678901234',
        password='password',
        first_name='David',
        last_name='Brown',
    )

    Sarah = User(
        username='sarah.davis@example.com',
        email='sarah.davis@example.com',
        phone_number='6789012345',
        password='password',
        first_name='Sarah',
        last_name='Davis',
    )

    Chris = User(
        username='chris.miller@example.com',
        email='chris.miller@example.com',
        phone_number='7890123456',
        password='password',
        first_name='Chris',
        last_name='Miller',
    )

    Laura = User(
        username='laura.wilson@example.com',
        email='laura.wilson@example.com',
        phone_number='8901234567',
        password='password',
        first_name='Laura',
        last_name='Wilson',
    )

    Joshua = User(
        username='joshua.moore@example.com',
        email='joshua.moore@example.com',
        phone_number='9012345678',
        password='password',
        first_name='Joshua',
        last_name='Moore',
    )

    Olivia = User(
        username='olivia.taylor@example.com',
        email='olivia.taylor@example.com',
        phone_number='0123456789',
        password='password',
        first_name='Olivia',
        last_name='Taylor',
    )

    # db.session.add(demo)
    # db.session.add(marnie)
    # db.session.add(bobbie)
    db.session.add(John)
    # db.session.add(Jane)
    # db.session.add(Michael)
    # db.session.add(Emily)
    # db.session.add(David)
    # db.session.add(Sarah)
    # db.session.add(Chris)
    # db.session.add(Laura)
    # db.session.add(Joshua)
    # db.session.add(Olivia)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))
        
    db.session.commit()
