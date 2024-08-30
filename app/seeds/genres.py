from app.models import db, Genre, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_genres():
    drama = Genre(
        genre_name='Drama',
    )

    comedy = Genre(
        genre_name='Comedy',
    )

    horror = Genre(
        genre_name='Horror',
    )

    sci_fi = Genre(
        genre_name='Sci-Fi',
    )


    historical = Genre(
        genre_name='Historical',
    )


    db.session.add(drama)
    db.session.add(comedy)
    db.session.add(horror)
    db.session.add(sci_fi)
    db.session.add(historical)

    
    
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_genres():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.genres RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM genres"))
        
    db.session.commit()
