from app.models import db, environment, SCHEMA, User, Genre

from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_user_genres():
    # Fetch users and genres from the database
    
    drama = Genre.query.get(1)
    comedy = Genre.query.get(2)
    horror = Genre.query.get(3)
    sci_fi = Genre.query.get(4)
    historical = Genre.query.get(5)
   

    # Associate genres with users
    # First 40 users associated with both Drama and Comedy
    for i in range(1, 41):
        user = User.query.get(i)
        user.genres.append(drama)
        user.genres.append(comedy)

    # Next 10 users associated with both Horror and Sci-Fi
    for i in range(41, 51):
        user = User.query.get(i)
        user.genres.append(horror)
        user.genres.append(sci_fi)

    # Next 30 users associated with Historical
    for i in range(51, 81):
        user = User.query.get(i)
        user.genres.append(historical)

    # Alternate genres for the remaining 20 users
    for i in range(81, 101):
        user = User.query.get(i)
        if i % 2 == 0:
            user.genres.append(drama)
        else:
            user.genres.append(comedy)
        if i % 3 == 0:
            user.genres.append(horror)
        elif i % 5 == 0:
            user.genres.append(sci_fi)

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
