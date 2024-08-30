from app.models import db, Referral, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_referrals():
    
    referral_0 = Referral(
    shortlist_id = 2,
    referred_id = 6,
    date_referred = db.func.now()
    )

    referral_1 = Referral(
    shortlist_id=1,  # The ID of the shortlist "NYC Editors for Indie Documentary"
    referred_id=12,  # User ID of a matching user
    date_referred=db.func.now()
    )

    referral_2 = Referral(
        shortlist_id=1,
        referred_id=15,
        date_referred=db.func.now()
    )

    referral_3 = Referral(
        shortlist_id=1,
        referred_id=23,
        date_referred=db.func.now()
    )

    referral_4 = Referral(
        shortlist_id=1,
        referred_id=34,
        date_referred=db.func.now()
    )

    referral_5 = Referral(
        shortlist_id=1,
        referred_id=45,
        date_referred=db.func.now()
    )

    referral_6 = Referral(
        shortlist_id=1,
        referred_id=56,
        date_referred=db.func.now()
    )
    


   
    db.session.add_all([referral_0,referral_1,referral_2,referral_3,referral_4,referral_5,referral_6])
    
    
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_referrals():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.referrals RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM referrals"))
        
    db.session.commit()
