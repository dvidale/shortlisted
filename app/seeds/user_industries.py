from app.models import db, environment, SCHEMA, User, Industry_Area

from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_user_industries():
    # Fetch users and industry areas from the database
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




    scripted_television = Industry_Area.query.get(1)
    unscripted_television = Industry_Area.query.get(2)
    dramatic_film = Industry_Area.query.get(3)
    documentary = Industry_Area.query.get(4)
    commercial = Industry_Area.query.get(5)
    animation = Industry_Area.query.get(6)


    # Associate industry areas with users
    # Industry Area Associations
    aaliyah.industry_areas.extend([scripted_television, dramatic_film])  # Aaliyah - Scripted Television, Dramatic Film
    brianna.industry_areas.extend([unscripted_television, documentary])  # Brianna - Unscripted Television, Documentary
    ciara.industry_areas.extend([commercial, animation])  # Ciara - Commercial, Animation
    deja.industry_areas.extend([scripted_television, unscripted_television])  # Deja - Scripted Television, Unscripted Television
    emani.industry_areas.extend([dramatic_film, documentary])  # Emani - Dramatic Film, Documentary
    faith.industry_areas.extend([commercial, animation])  # Faith - Commercial, Animation
    gabrielle.industry_areas.extend([scripted_television, dramatic_film])  # Gabrielle - Scripted Television, Dramatic Film
    halle.industry_areas.extend([unscripted_television, documentary])  # Halle - Unscripted Television, Documentary
    imani.industry_areas.extend([commercial, animation])  # Imani - Commercial, Animation
    jada.industry_areas.extend([scripted_television, unscripted_television])  # Jada - Scripted Television, Unscripted Television

    aaron_z.industry_areas.extend([dramatic_film, documentary])  # Aaron - Dramatic Film, Documentary
    brandon.industry_areas.extend([commercial, animation])  # Brandon - Commercial, Animation
    caleb.industry_areas.extend([scripted_television, dramatic_film])  # Caleb - Scripted Television, Dramatic Film
    darius.industry_areas.extend([unscripted_television, documentary])  # Darius - Unscripted Television, Documentary
    elijah.industry_areas.extend([commercial, animation])  # Elijah - Commercial, Animation
    franklin.industry_areas.extend([scripted_television, unscripted_television])  # Franklin - Scripted Television, Unscripted Television
    gregory.industry_areas.extend([dramatic_film, documentary])  # Gregory - Dramatic Film, Documentary
    howard.industry_areas.extend([commercial, animation])  # Howard - Commercial, Animation
    isaiah.industry_areas.extend([scripted_television, dramatic_film])  # Isaiah - Scripted Television, Dramatic Film
    jason.industry_areas.extend([unscripted_television, documentary])  # Jason - Unscripted Television, Documentary

    arjun.industry_areas.extend([commercial, animation])  # Arjun - Commercial, Animation
    bilal.industry_areas.extend([scripted_television, dramatic_film])  # Bilal - Scripted Television, Dramatic Film
    chetan.industry_areas.extend([unscripted_television, documentary])  # Chetan - Unscripted Television, Documentary
    dev.industry_areas.extend([commercial, animation])  # Dev - Commercial, Animation
    eshan.industry_areas.extend([scripted_television, unscripted_television])  # Eshan - Scripted Television, Unscripted Television
    faisal.industry_areas.extend([dramatic_film, documentary])  # Faisal - Dramatic Film, Documentary
    gautam.industry_areas.extend([commercial, animation])  # Gautam - Commercial, Animation
    harish.industry_areas.extend([scripted_television, dramatic_film])  # Harish - Scripted Television, Dramatic Film
    imran.industry_areas.extend([unscripted_television, documentary])  # Imran - Unscripted Television, Documentary
    jai.industry_areas.extend([commercial, animation])  # Jai - Commercial, Animation

    kavya.industry_areas.extend([scripted_television, unscripted_television])  # Kavya - Scripted Television, Unscripted Television
    lata.industry_areas.extend([dramatic_film, documentary])  # Lata - Dramatic Film, Documentary
    meera.industry_areas.extend([commercial, animation])  # Meera - Commercial, Animation
    naina.industry_areas.extend([scripted_television, dramatic_film])  # Naina - Scripted Television, Dramatic Film
    oorja.industry_areas.extend([unscripted_television, documentary])  # Oorja - Unscripted Television, Documentary
    pooja.industry_areas.extend([commercial, animation])  # Pooja - Commercial, Animation
    qadira.industry_areas.extend([scripted_television, unscripted_television])  # Qadira - Scripted Television, Unscripted Television
    rani.industry_areas.extend([dramatic_film, documentary])  # Rani - Dramatic Film, Documentary
    sanya.industry_areas.extend([commercial, animation])  # Sanya - Commercial, Animation
    tanvi.industry_areas.extend([scripted_television, dramatic_film])  # Tanvi - Scripted Television, Dramatic Film

    elena.industry_areas.extend([unscripted_television, documentary])  # Elena - Unscripted Television, Documentary
    frida.industry_areas.extend([commercial, animation])  # Frida - Commercial, Animation
    gabriela.industry_areas.extend([scripted_television, unscripted_television])  # Gabriela - Scripted Television, Unscripted Television
    helena.industry_areas.extend([dramatic_film, documentary])  # Helena - Dramatic Film, Documentary
    isabella.industry_areas.extend([commercial, animation])  # Isabella - Commercial, Animation
    juana.industry_areas.extend([scripted_television, dramatic_film])  # Juana - Scripted Television, Dramatic Film
    karla.industry_areas.extend([unscripted_television, documentary])  # Karla - Unscripted Television, Documentary
    lucia.industry_areas.extend([commercial, animation])  # Lucia - Commercial, Animation
    mariana.industry_areas.extend([scripted_television, unscripted_television])  # Mariana - Scripted Television, Unscripted Television
    natalia.industry_areas.extend([dramatic_film, documentary])  # Natalia - Dramatic Film, Documentary

    olivia.industry_areas.extend([commercial, animation])  # Olivia - Commercial, Animation
    penelope.industry_areas.extend([scripted_television, dramatic_film])  # Penelope - Scripted Television, Dramatic Film
    quinn.industry_areas.extend([unscripted_television, documentary])  # Quinn - Unscripted Television, Documentary
    rachel.industry_areas.extend([commercial, animation])  # Rachel - Commercial, Animation
    sophia.industry_areas.extend([scripted_television, unscripted_television])  # Sophia - Scripted Television, Unscripted Television
    tiffany.industry_areas.extend([dramatic_film, documentary])  # Tiffany - Dramatic Film, Documentary
    ursula.industry_areas.extend([commercial, animation])  # Ursula - Commercial, Animation
    victoria.industry_areas.extend([scripted_television, dramatic_film])  # Victoria - Scripted Television, Dramatic Film
    wendy.industry_areas.extend([unscripted_television, documentary])  # Wendy - Unscripted Television, Documentary
    xena.industry_areas.extend([commercial, animation])  # Xena - Commercial, Animation

    aaron_miller.industry_areas.extend([scripted_television, unscripted_television])  # Aaron - Scripted Television, Unscripted Television
    brian.industry_areas.extend([dramatic_film, documentary])  # Brian - Dramatic Film, Documentary
    cameron.industry_areas.extend([commercial, animation])  # Cameron - Commercial, Animation
    dylan.industry_areas.extend([scripted_television, dramatic_film])  # Dylan - Scripted Television, Dramatic Film
    ethan.industry_areas.extend([unscripted_television, documentary])  # Ethan - Unscripted Television, Documentary
    felix.industry_areas.extend([commercial, animation])  # Felix - Commercial, Animation
    gavin.industry_areas.extend([scripted_television, unscripted_television])  # Gavin - Scripted Television, Unscripted Television
    henry.industry_areas.extend([dramatic_film, documentary])  # Henry - Dramatic Film, Documentary
    ian.industry_areas.extend([commercial, animation])  # Ian - Commercial, Animation
    jack.industry_areas.extend([scripted_television, dramatic_film])  # Jack - Scripted Television, Dramatic Film




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
