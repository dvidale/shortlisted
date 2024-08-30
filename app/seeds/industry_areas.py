from app.models import db, Industry_Area, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_industry_areas():
    scripted_television = Industry_Area(
    industry_area='Scripted Television',
    )

    unscripted_television = Industry_Area(
        industry_area='Unscripted Television',
    )

    dramatic_film = Industry_Area(
        industry_area='Dramatic Film',
    )

    documentary = Industry_Area(
        industry_area='Documentary',
    )

    commercial = Industry_Area(
        industry_area='Commercial',
    )

    animation = Industry_Area(
        industry_area = 'Animation',
    )



    db.session.add(scripted_television)
    db.session.add(unscripted_television)
    db.session.add(dramatic_film)
    db.session.add(documentary)
    db.session.add(commercial)
    db.session.add(animation)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_industry_areas():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.industry_areas RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM industry_areas"))
        
    db.session.commit()
