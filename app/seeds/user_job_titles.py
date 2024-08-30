from app.models import db,  environment, SCHEMA, User, Job_Title



from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_user_job_titles():
   
    editor = Job_Title.query.get(1)
    assistant_editor = Job_Title.query.get(2)

    
    aaliyah = User.query.filter_by(username='aaliyah.walker@example.com').first()
    brianna = User.query.filter_by(username='brianna.jones@example.com').first()
    ciara = User.query.filter_by(username='ciara.taylor@example.com').first()
    deja = User.query.filter_by(username='deja.harris@example.com').first()
    emani = User.query.filter_by(username='emani.brown@example.com').first()
    faith = User.query.filter_by(username='faith.davis@example.com').first()
    gabrielle = User.query.filter_by(username='gabrielle.white@example.com').first()
    halle = User.query.filter_by(username='halle.jackson@example.com').first()
    imani = User.query.filter_by(username='imani.clark@example.com').first()
    jada = User.query.filter_by(username='jada.lee@example.com').first()

    aaron_z = User.query.filter_by(username='aaron.mitchell@example.com').first()
    brandon = User.query.filter_by(username='brandon.carter@example.com').first()
    caleb = User.query.filter_by(username='caleb.richardson@example.com').first()
    darius = User.query.filter_by(username='darius.scott@example.com').first()
    elijah = User.query.filter_by(username='elijah.thomas@example.com').first()
    franklin = User.query.filter_by(username='franklin.bailey@example.com').first()
    gregory = User.query.filter_by(username='gregory.daniels@example.com').first()
    howard = User.query.filter_by(username='howard.foster@example.com').first()
    isaiah = User.query.filter_by(username='isaiah.griffin@example.com').first()
    jason = User.query.filter_by(username='jason.hayes@example.com').first()

    arjun = User.query.filter_by(username='arjun.patel@example.com').first()
    bilal = User.query.filter_by(username='bilal.khan@example.com').first()
    chetan = User.query.filter_by(username='chetan.sharma@example.com').first()
    dev = User.query.filter_by(username='dev.raj@example.com').first()
    eshan = User.query.filter_by(username='eshan.mehta@example.com').first()
    faisal = User.query.filter_by(username='faisal.naidu@example.com').first()
    gautam = User.query.filter_by(username='gautam.anand@example.com').first()
    harish = User.query.filter_by(username='harish.joshi@example.com').first()
    imran = User.query.filter_by(username='imran.qureshi@example.com').first()
    jai = User.query.filter_by(username='jai.verma@example.com').first()

    kavya = User.query.filter_by(username='kavya.malhotra@example.com').first()
    lata = User.query.filter_by(username='lata.nair@example.com').first()
    meera = User.query.filter_by(username='meera.patel@example.com').first()
    naina = User.query.filter_by(username='naina.raj@example.com').first()
    oorja = User.query.filter_by(username='oorja.singh@example.com').first()
    pooja = User.query.filter_by(username='pooja.kumar@example.com').first()
    qadira = User.query.filter_by(username='qadira.tiwari@example.com').first()
    rani = User.query.filter_by(username='rani.ahuja@example.com').first()
    sanya = User.query.filter_by(username='sanya.mehta@example.com').first()
    tanvi = User.query.filter_by(username='tanvi.varma@example.com').first()

    elena = User.query.filter_by(username='elena.santos@example.com').first()
    frida = User.query.filter_by(username='frida.torres@example.com').first()
    gabriela = User.query.filter_by(username='gabriela.uribe@example.com').first()
    helena = User.query.filter_by(username='helena.velasquez@example.com').first()
    isabella = User.query.filter_by(username='isabella.williams@example.com').first()
    juana = User.query.filter_by(username='juana.ximenez@example.com').first()
    karla = User.query.filter_by(username='karla.ybarra@example.com').first()
    lucia = User.query.filter_by(username='lucia.zaragoza@example.com').first()
    mariana = User.query.filter_by(username='mariana.alonso@example.com').first()
    natalia = User.query.filter_by(username='natalia.barrera@example.com').first()

    olivia = User.query.filter_by(username='olivia.clark@example.com').first()
    penelope = User.query.filter_by(username='penelope.dunn@example.com').first()
    quinn = User.query.filter_by(username='quinn.ellis@example.com').first()
    rachel = User.query.filter_by(username='rachel.ford@example.com').first()
    sophia = User.query.filter_by(username='sophia.gray@example.com').first()
    tiffany = User.query.filter_by(username='tiffany.hunt@example.com').first()
    ursula = User.query.filter_by(username='ursula.ingram@example.com').first()
    victoria = User.query.filter_by(username='victoria.jones@example.com').first()
    wendy = User.query.filter_by(username='wendy.knight@example.com').first()
    xena = User.query.filter_by(username='xena.lambert@example.com').first()

    aaron_miller = User.query.filter_by(username='aaron.miller@example.com').first()
    brian = User.query.filter_by(username='brian.nelson@example.com').first()
    cameron = User.query.filter_by(username='cameron.owens@example.com').first()
    dylan = User.query.filter_by(username='dylan.parker@example.com').first()
    ethan = User.query.filter_by(username='ethan.quinn@example.com').first()
    felix = User.query.filter_by(username='felix.ross@example.com').first()
    gavin = User.query.filter_by(username='gavin.stone@example.com').first()
    henry = User.query.filter_by(username='henry.taylor@example.com').first()
    ian = User.query.filter_by(username='ian.underwood@example.com').first()
    jack = User.query.filter_by(username='jack.vance@example.com').first()


   # Single Job Title Associations
    aaliyah.job_titles.append(editor)  # Aaliyah - Editor
    brianna.job_titles.append(assistant_editor)  # Brianna - Assistant Editor
    ciara.job_titles.append(editor)  # Ciara - Editor
    deja.job_titles.append(assistant_editor)  # Deja - Assistant Editor
    emani.job_titles.append(editor)  # Emani - Editor
    faith.job_titles.append(assistant_editor)  # Faith - Assistant Editor
    gabrielle.job_titles.append(editor)  # Gabrielle - Editor
    halle.job_titles.append(assistant_editor)  # Halle - Assistant Editor
    imani.job_titles.append(editor)  # Imani - Editor
    jada.job_titles.append(assistant_editor)  # Jada - Assistant Editor

    aaron_z.job_titles.append(editor)  # Aaron - Editor
    brandon.job_titles.append(assistant_editor)  # Brandon - Assistant Editor
    caleb.job_titles.append(editor)  # Caleb - Editor
    darius.job_titles.append(assistant_editor)  # Darius - Assistant Editor
    elijah.job_titles.append(editor)  # Elijah - Editor
    franklin.job_titles.append(assistant_editor)  # Franklin - Assistant Editor
    gregory.job_titles.append(editor)  # Gregory - Editor
    howard.job_titles.append(assistant_editor)  # Howard - Assistant Editor
    isaiah.job_titles.append(editor)  # Isaiah - Editor
    jason.job_titles.append(assistant_editor)  # Jason - Assistant Editor

    # Double Job Title Associations
    arjun.job_titles.extend([editor, assistant_editor])  # Arjun - Editor, Assistant Editor
    bilal.job_titles.extend([editor, assistant_editor])  # Bilal - Editor, Assistant Editor
    chetan.job_titles.extend([editor, assistant_editor])  # Chetan - Editor, Assistant Editor
    dev.job_titles.extend([editor, assistant_editor])  # Dev - Editor, Assistant Editor
    eshan.job_titles.extend([editor, assistant_editor])  # Eshan - Editor, Assistant Editor
    faisal.job_titles.extend([editor, assistant_editor])  # Faisal - Editor, Assistant Editor
    gautam.job_titles.extend([editor, assistant_editor])  # Gautam - Editor, Assistant Editor
    harish.job_titles.extend([editor, assistant_editor])  # Harish - Editor, Assistant Editor
    imran.job_titles.extend([editor, assistant_editor])  # Imran - Editor, Assistant Editor
    jai.job_titles.extend([editor, assistant_editor])  # Jai - Editor, Assistant Editor

    kavya.job_titles.extend([editor, assistant_editor])  # Kavya - Editor, Assistant Editor
    lata.job_titles.extend([editor, assistant_editor])  # Lata - Editor, Assistant Editor
    meera.job_titles.extend([editor, assistant_editor])  # Meera - Editor, Assistant Editor
    naina.job_titles.extend([editor, assistant_editor])  # Naina - Editor, Assistant Editor
    oorja.job_titles.extend([editor, assistant_editor])  # Oorja - Editor, Assistant Editor
    pooja.job_titles.extend([editor, assistant_editor])  # Pooja - Editor, Assistant Editor
    qadira.job_titles.extend([editor, assistant_editor])  # Qadira - Editor, Assistant Editor
    rani.job_titles.extend([editor, assistant_editor])  # Rani - Editor, Assistant Editor
    sanya.job_titles.extend([editor, assistant_editor])  # Sanya - Editor, Assistant Editor
    tanvi.job_titles.extend([editor, assistant_editor])  # Tanvi - Editor, Assistant Editor

    elena.job_titles.extend([editor, assistant_editor])  # Elena - Editor, Assistant Editor
    frida.job_titles.extend([editor, assistant_editor])  # Frida - Editor, Assistant Editor
    gabriela.job_titles.extend([editor, assistant_editor])  # Gabriela - Editor, Assistant Editor
    helena.job_titles.extend([editor, assistant_editor])  # Helena - Editor, Assistant Editor
    isabella.job_titles.extend([editor, assistant_editor])  # Isabella - Editor, Assistant Editor
    juana.job_titles.extend([editor, assistant_editor])  # Juana - Editor, Assistant Editor
    karla.job_titles.extend([editor, assistant_editor])  # Karla - Editor, Assistant Editor
    lucia.job_titles.extend([editor, assistant_editor])  # Lucia - Editor, Assistant Editor
    mariana.job_titles.extend([editor, assistant_editor])  # Mariana - Editor, Assistant Editor
    natalia.job_titles.extend([editor, assistant_editor])  # Natalia - Editor, Assistant Editor

    olivia.job_titles.extend([editor, assistant_editor])  # Olivia - Editor, Assistant Editor
    penelope.job_titles.extend([editor, assistant_editor])  # Penelope - Editor, Assistant Editor
    quinn.job_titles.extend([editor, assistant_editor])  # Quinn - Editor, Assistant Editor
    rachel.job_titles.extend([editor, assistant_editor])  # Rachel - Editor, Assistant Editor
    sophia.job_titles.extend([editor, assistant_editor])  # Sophia - Editor, Assistant Editor
    tiffany.job_titles.extend([editor, assistant_editor])  # Tiffany - Editor, Assistant Editor
    ursula.job_titles.extend([editor, assistant_editor])  # Ursula - Editor, Assistant Editor
    victoria.job_titles.extend([editor, assistant_editor])  # Victoria - Editor, Assistant Editor
    wendy.job_titles.extend([editor, assistant_editor])  # Wendy - Editor, Assistant Editor
    xena.job_titles.extend([editor, assistant_editor])  # Xena - Editor, Assistant Editor

    aaron_miller.job_titles.extend([editor, assistant_editor])  # Aaron - Editor, Assistant Editor
    brian.job_titles.extend([editor, assistant_editor])  # Brian - Editor, Assistant Editor
    cameron.job_titles.extend([editor, assistant_editor])  # Cameron - Editor, Assistant Editor
    dylan.job_titles.extend([editor, assistant_editor])  # Dylan - Editor, Assistant Editor
    ethan.job_titles.extend([editor, assistant_editor])  # Ethan - Editor, Assistant Editor
    felix.job_titles.extend([editor, assistant_editor])  # Felix - Editor, Assistant Editor
    gavin.job_titles.extend([editor, assistant_editor])  # Gavin - Editor, Assistant Editor
    henry.job_titles.extend([editor, assistant_editor])  # Henry - Editor, Assistant Editor
    ian.job_titles.extend([editor, assistant_editor])  # Ian - Editor, Assistant Editor
    jack.job_titles.extend([editor, assistant_editor])  # Jack - Editor, Assistant Editor



    
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
