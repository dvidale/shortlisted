from app.models import db,  environment, SCHEMA, User, Job_Title


from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_user_job_titles():
    # Fetch users and job titles from the database
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

    editor = Job_Title.query.get(1)
    assistant_editor = Job_Title.query.get(2)

    # Associate job titles with users
    john.job_titles.append(editor)  # John - Editor
    john.job_titles.append(assistant_editor)  # John - Assistant Editor

    jane.job_titles.append(assistant_editor)  # Jane - Assistant Editor
    jane.job_titles.append(editor)  # Jane - Editor

    michael.job_titles.append(editor)  # Michael - Editor
    michael.job_titles.append(assistant_editor)  # Michael - Assistant Editor

    emily.job_titles.append(assistant_editor)  # Emily - Assistant Editor
    emily.job_titles.append(editor)  # Emily - Editor

    david.job_titles.append(editor)  # David - Editor
    david.job_titles.append(assistant_editor)  # David - Assistant Editor

    sarah.job_titles.append(assistant_editor)  # Sarah - Assistant Editor

    chris.job_titles.append(editor)  # Chris - Editor

    laura.job_titles.append(assistant_editor)  # Laura - Assistant Editor

    joshua.job_titles.append(editor)  # Joshua - Editor

    olivia.job_titles.append(assistant_editor)  # Olivia - Assistant Editor

    # Commit the changes to the database
    db.session.commit()



# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_user_job_titles():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.user_job_titles RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM user_job_titles"))
        
    db.session.commit()
