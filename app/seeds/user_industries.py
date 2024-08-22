from app.models import db, environment, SCHEMA, User, Industry_Area

from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_user_industries():
    # Fetch users and industry areas from the database
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

    scripted_tv = Industry_Area.query.get(1)
    unscripted_tv = Industry_Area.query.get(2)
    dramatic_film = Industry_Area.query.get(3)
    documentary = Industry_Area.query.get(4)
    commercial = Industry_Area.query.get(5)

    # Associate industry areas with users
    john.industry_areas.append(scripted_tv)  # John - Scripted Television
    john.industry_areas.append(unscripted_tv)  # John - Unscripted Television

    jane.industry_areas.append(dramatic_film)  # Jane - Dramatic Film
    jane.industry_areas.append(documentary)  # Jane - Documentary

    michael.industry_areas.append(scripted_tv)  # Michael - Scripted Television
    michael.industry_areas.append(commercial)  # Michael - Commercial

    emily.industry_areas.append(unscripted_tv)  # Emily - Unscripted Television
    emily.industry_areas.append(dramatic_film)  # Emily - Dramatic Film

    david.industry_areas.append(documentary)  # David - Documentary
    david.industry_areas.append(commercial)  # David - Commercial

    sarah.industry_areas.append(scripted_tv)  # Sarah - Scripted Television

    chris.industry_areas.append(unscripted_tv)  # Chris - Unscripted Television

    laura.industry_areas.append(dramatic_film)  # Laura - Dramatic Film

    joshua.industry_areas.append(documentary)  # Joshua - Documentary

    olivia.industry_areas.append(commercial)  # Olivia - Commercial

    # Commit the changes to the database
    db.session.commit()



# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_user_industries():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.user_industries RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM user_industries"))
        
    db.session.commit()
