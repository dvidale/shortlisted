from app.models import db, Comment, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_comments():
    
    aaliyah_comment = Comment(
    shortlist_id=2,
    commenter_id=1,
    referral_id = 1,
    text='Hey Faith, this gig is right down your lane!',
    createdAt = db.func.now(),
    updatedAt = db.func.now()
    )
    faith_comment = Comment(
    shortlist_id =2,
    commenter_id = 6,
    referral_id = 1,
    text='This is so perfect! I come back in town the week before!',
    createdAt = db.func.now(),
    updatedAt = db.func.now()
    )
    
    comment_2 = Comment(
        shortlist_id=1,
        commenter_id=12,  # Referred user
        referral_id=2,  # Corresponding referral ID
        text="Can you provide more details on the expected workload and deadlines?",
        createdAt=db.func.now(),
        updatedAt=db.func.now()
    )

    comment_3 = Comment(
        shortlist_id=1,
        commenter_id=15,  # Referred user
        referral_id=3,  # Corresponding referral ID
        text="Is there any flexibility with the start date?",
        createdAt=db.func.now(),
        updatedAt=db.func.now()
    )

    comment_4 = Comment(
        shortlist_id=1,
        commenter_id=23,  # Referred user
        referral_id=4,  # Corresponding referral ID
        text="Could you clarify the documentary's subject matter a bit more?",
        createdAt=db.func.now(),
        updatedAt=db.func.now()
    )

    comment_5 = Comment(
        shortlist_id=1,
        commenter_id=34,  # Referred user
        referral_id=5,  # Corresponding referral ID
        text="Are there any specific software requirements for editing?",
        createdAt=db.func.now(),
        updatedAt=db.func.now()
    )

    comment_6 = Comment(
        shortlist_id=1,
        commenter_id=45,  # Referred user
        referral_id=6,  # Corresponding referral ID
        text="Will there be opportunities for creative input during the editing process?",
        createdAt=db.func.now(),
        updatedAt=db.func.now()
    )

    comment_7 = Comment(
        shortlist_id=1,
        commenter_id=56,  # Referred user
        referral_id=7,  # Corresponding referral ID
        text="Is the editing team remote or on-site?",
        createdAt=db.func.now(),
        updatedAt=db.func.now()
    )

    response_2 = Comment(
        shortlist_id=1,
        commenter_id=1,  # Creator of the shortlist
        referral_id=2,
        text="The workload is fairly balanced with set deadlines every two weeks. The entire project is expected to be completed by August 15th.",
        createdAt=db.func.now(),
        updatedAt=db.func.now()
    )

    response_3 = Comment(
        shortlist_id=1,
        commenter_id=1,  # Creator of the shortlist
        referral_id=3,
        text="The start date is somewhat flexible, but we are aiming for early February. Let us know your availability.",
        createdAt=db.func.now(),
        updatedAt=db.func.now()
    )

    response_4 = Comment(
        shortlist_id=1,
        commenter_id=1,  # Creator of the shortlist
        referral_id=4,
        text="The documentary focuses on various social justice issues in NYC, with interviews and on-the-ground footage.",
        createdAt=db.func.now(),
        updatedAt=db.func.now()
    )

    response_5 = Comment(
        shortlist_id=1,
        commenter_id=1,  # Creator of the shortlist
        referral_id=5,
        text="We prefer editors experienced with Adobe Premiere Pro and DaVinci Resolve, but we are open to other platforms if necessary.",
        createdAt=db.func.now(),
        updatedAt=db.func.now()
    )

    response_6 = Comment(
        shortlist_id=1,
        commenter_id=1,  # Creator of the shortlist
        referral_id=6,
        text="Yes, there will be plenty of opportunities for creative input. The director encourages collaboration!",
        createdAt=db.func.now(),
        updatedAt=db.func.now()
    )

    response_7 = Comment(
        shortlist_id=1,
        commenter_id=1,  # Creator of the shortlist
        referral_id=7,
        text="The editing team will primarily be on-site in NYC, but remote work is an option depending on circumstances.",
        createdAt=db.func.now(),
        updatedAt=db.func.now()
    )

    comment_variables = [
        aaliyah_comment,
        faith_comment,
        comment_2,
        comment_3,
        comment_4,
        comment_5,
        comment_6,
        comment_7,
        response_2,
        response_3,
        response_4,
        response_5,
        response_6,
        response_7
    ]

    db.session.add_all(comment_variables)
    
    
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
