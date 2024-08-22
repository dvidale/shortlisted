from app.models import db, environment, SCHEMA, User, Genre

from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_user_genres():
    # Fetch users and genres from the database
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

    drama = Genre.query.get(1)
    comedy = Genre.query.get(2)
    horror = Genre.query.get(3)
    sci_fi = Genre.query.get(4)
    animation = Genre.query.get(5)
    historical = Genre.query.get(6)

    # Associate genres with users
    john.genres.append(drama)  # John - Drama
    john.genres.append(comedy)  # John - Comedy

    jane.genres.append(drama)  # Jane - Drama
    jane.genres.append(comedy)  # Jane - Comedy

    michael.genres.append(drama)  # Michael - Drama
    michael.genres.append(comedy)  # Michael - Comedy

    emily.genres.append(drama)  # Emily - Drama
    emily.genres.append(comedy)  # Emily - Comedy

    david.genres.append(horror)  # David - Horror
    david.genres.append(sci_fi)  # David - Sci-Fi

    sarah.genres.append(animation)  # Sarah - Animation
    chris.genres.append(animation)  # Chris - Animation
    laura.genres.append(animation)  # Laura - Animation

    joshua.genres.append(historical)  # Joshua - Historical
    olivia.genres.append(historical)  # Olivia - Historical

    # Commit the changes to the database
    db.session.commit()



# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_user_genres():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.user_genres RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM user_genres"))
        
    db.session.commit()
