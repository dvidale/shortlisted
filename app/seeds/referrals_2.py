from app.models import db, Referral, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_referrals_2():
    
    referral_7 = Referral(
    shortlist_id = 3,
    referred_id = 23,
    date_referred = db.func.now()
    )

    referral_8 = Referral(
    shortlist_id=3, 
    referred_id=25,  # User ID of a matching user
    date_referred=db.func.now()
    )

    referral_9 = Referral(
        shortlist_id=3,
        referred_id=29,
        date_referred=db.func.now()
    )

    referral_10 = Referral(
        shortlist_id=3,
        referred_id=31,
        date_referred=db.func.now()
    )

    referral_11 = Referral(
        shortlist_id=3,
        referred_id=35,
        date_referred=db.func.now()
    )

    referral_12 = Referral(
        shortlist_id=3,
        referred_id=37,
        date_referred=db.func.now()
    )

    referral_13 = Referral(
        shortlist_id=4,
        referred_id=43,
        date_referred=db.func.now()
    )
    
    referral_14 = Referral(
        shortlist_id=4,
        referred_id=47,
        date_referred=db.func.now()
    )

    referral_15 = Referral(
        shortlist_id=4,
        referred_id=59,
        date_referred=db.func.now()
    )
    
    referral_16 = Referral(
        shortlist_id=4,
        referred_id=61,
        date_referred=db.func.now()
    )

    referral_17 = Referral(
        shortlist_id=4,
        referred_id=65,
        date_referred=db.func.now()
    )

  

   
    db.session.add_all([referral_7,referral_8,referral_9,referral_10,referral_11,referral_12,referral_13,referral_14,referral_15,referral_16,referral_17])
    
    
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_referrals_2():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.referrals RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM referrals"))
        
    db.session.commit()
