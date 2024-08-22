from app.models import db, Job_Title, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_job_titles():
    editor = Job_Title(
        job_title='Editor',
    )
    assist_editor=Job_Title(
        job_title='Assistant Editor'
    )


    db.session.add(editor)
    db.session.add(assist_editor)
    
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_job_titles():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.job_titles RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM job_titles"))
        
    db.session.commit()
