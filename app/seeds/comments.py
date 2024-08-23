from app.models import db, Comment, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_comments():
    
    john_comment = Comment(
    shortlist_id=1,
    commenter_id=4,
    referral_id = 1,
    text='Hey Mike, this gig is right down your lane!',
    createdAt = db.func.now(),
    updatedAt = db.func.now()
    )
    mike_comment = Comment(
    shortlist_id =1,
    commenter_id = 6,
    referral_id = 1,
    text='This is so perfect! I come back in town the week before!',
    createdAt = db.func.now(),
    updatedAt = db.func.now()
)
   
    db.session.add(john_comment)
    db.session.add(mike_comment)
    
    
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_comments():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.comments RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM comments"))
        
    db.session.commit()
