from app.models import db,  environment, SCHEMA, User, Job_Title
from app.models import user_job_title


from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_user_job_titles():
   
    editor = Job_Title.query.get(1)
    assistant_editor = Job_Title.query.get(2)

    
    aaliyah = User.query.get(1)
    aaliyah.job_titles.append(editor) # Aaliyah - Editor
    aaliyah.job_titles.append(assistant_editor) # Aaliyah - Assistant Editor

    brianna = User.query.get(2)
    brianna.job_titles.append(editor) # Brianna - Editor

    ciara = User.query.get(3)
    ciara.job_titles.append(editor) # Ciara - Editor
    ciara.job_titles.append(assistant_editor) # Ciara - Assistant Editor

    deja = User.query.get(4)
    deja.job_titles.append(editor) # Deja - Editor

    emani = User.query.get(5)
    emani.job_titles.append(editor) # Emani - Editor
    emani.job_titles.append(assistant_editor) # Emani - Assistant Editor

    faith = User.query.get(6)
    faith.job_titles.append(editor) # Faith - Editor

    gabrielle = User.query.get(7)
    gabrielle.job_titles.append(editor) # Gabrielle - Editor
    gabrielle.job_titles.append(assistant_editor) # Gabrielle - Assistant Editor

    halle = User.query.get(8)
    halle.job_titles.append(editor) # Halle - Editor

    imani = User.query.get(9)
    imani.job_titles.append(editor) # Imani - Editor
    imani.job_titles.append(assistant_editor) # Imani - Assistant Editor

    jada = User.query.get(10)
    jada.job_titles.append(editor) # Jada - Editor

    aaron = User.query.get(11)
    aaron.job_titles.append(editor) # Aaron - Editor
    aaron.job_titles.append(assistant_editor) # Aaron - Assistant Editor

    brandon = User.query.get(12)
    brandon.job_titles.append(editor) # Brandon - Editor

    caleb = User.query.get(13)
    caleb.job_titles.append(editor) # Caleb - Editor
    caleb.job_titles.append(assistant_editor) # Caleb - Assistant Editor

    darius = User.query.get(14)
    darius.job_titles.append(editor) # Darius - Editor

    elijah = User.query.get(15)
    elijah.job_titles.append(editor) # Elijah - Editor
    elijah.job_titles.append(assistant_editor) # Elijah - Assistant Editor

    franklin = User.query.get(16)
    franklin.job_titles.append(editor) # Franklin - Editor

    gregory = User.query.get(17)
    gregory.job_titles.append(editor) # Gregory - Editor
    gregory.job_titles.append(assistant_editor) # Gregory - Assistant Editor

    howard = User.query.get(18)
    howard.job_titles.append(editor) # Howard - Editor

    isaiah = User.query.get(19)
    isaiah.job_titles.append(editor) # Isaiah - Editor
    isaiah.job_titles.append(assistant_editor) # Isaiah - Assistant Editor

    jason = User.query.get(20)
    jason.job_titles.append(editor) # Jason - Editor

    
    arjun = User.query.get(21)
    arjun.job_titles.append(editor) # Arjun - Editor
    arjun.job_titles.append(assistant_editor) # Arjun - Assistant Editor

    bilal = User.query.get(22)
    bilal.job_titles.append(editor) # Bilal - Editor

    chetan = User.query.get(23)
    chetan.job_titles.append(editor) # Chetan - Editor
    chetan.job_titles.append(assistant_editor) # Chetan - Assistant Editor

    dev = User.query.get(24)
    dev.job_titles.append(editor) # Dev - Editor

    eshan = User.query.get(25)
    eshan.job_titles.append(editor) # Eshan - Editor
    eshan.job_titles.append(assistant_editor) # Eshan - Assistant Editor

    faisal = User.query.get(26)
    faisal.job_titles.append(editor) # Faisal - Editor

    gautam = User.query.get(27)
    gautam.job_titles.append(editor) # Gautam - Editor
    gautam.job_titles.append(assistant_editor) # Gautam - Assistant Editor

    harish = User.query.get(28)
    harish.job_titles.append(editor) # Harish - Editor

    imran = User.query.get(29)
    imran.job_titles.append(editor) # Imran - Editor
    imran.job_titles.append(assistant_editor) # Imran - Assistant Editor

    jai = User.query.get(30)
    jai.job_titles.append(editor) # Jai - Editor

    kavya = User.query.get(31)
    kavya.job_titles.append(editor) # Kavya - Editor
    kavya.job_titles.append(assistant_editor) # Kavya - Assistant Editor

    lata = User.query.get(32)
    lata.job_titles.append(editor) # Lata - Editor

    meera = User.query.get(33)
    meera.job_titles.append(editor) # Meera - Editor
    meera.job_titles.append(assistant_editor) # Meera - Assistant Editor

    naina = User.query.get(34)
    naina.job_titles.append(editor) # Naina - Editor

    oorja = User.query.get(35)
    oorja.job_titles.append(editor) # Oorja - Editor
    oorja.job_titles.append(assistant_editor) # Oorja - Assistant Editor

    pooja = User.query.get(36)
    pooja.job_titles.append(editor) # Pooja - Editor

    qadira = User.query.get(37)
    qadira.job_titles.append(editor) # Qadira - Editor
    qadira.job_titles.append(assistant_editor) # Qadira - Assistant Editor

    rani = User.query.get(38)
    rani.job_titles.append(editor) # Rani - Editor

    sanya = User.query.get(39)
    sanya.job_titles.append(editor) # Sanya - Editor
    sanya.job_titles.append(assistant_editor) # Sanya - Assistant Editor

    tanvi = User.query.get(40)
    tanvi.job_titles.append(editor) # Tanvi - Editor

    ulises = User.query.get(41)
    ulises.job_titles.append(editor) # Ulises - Editor

    vicente = User.query.get(42)
    vicente.job_titles.append(editor) # Vicente - Editor
    vicente.job_titles.append(assistant_editor) # Vicente - Assistant Editor

    william = User.query.get(43)
    william.job_titles.append(editor) # William - Editor

    xavier = User.query.get(44)
    xavier.job_titles.append(editor) # Xavier - Editor
    xavier.job_titles.append(assistant_editor) # Xavier - Assistant Editor

    yadiel = User.query.get(45)
    yadiel.job_titles.append(editor) # Yadiel - Editor

    zacarias = User.query.get(46)
    zacarias.job_titles.append(editor) # Zacarias - Editor
    zacarias.job_titles.append(assistant_editor) # Zacarias - Assistant Editor

    abel = User.query.get(47)
    abel.job_titles.append(editor) # Abel - Editor

    benicio = User.query.get(48)
    benicio.job_titles.append(editor) # Benicio - Editor
    benicio.job_titles.append(assistant_editor) # Benicio - Assistant Editor

    cesar = User.query.get(49)
    cesar.job_titles.append(editor) # Cesar - Editor

    diego = User.query.get(50)
    diego.job_titles.append(editor) # Diego - Editor
    diego.job_titles.append(assistant_editor) # Diego - Assistant Editor

    elena = User.query.get(51)
    elena.job_titles.append(editor) # Elena - Editor

    frida = User.query.get(52)
    frida.job_titles.append(editor) # Frida - Editor
    frida.job_titles.append(assistant_editor) # Frida - Assistant Editor

    gabriela = User.query.get(53)
    gabriela.job_titles.append(editor) # Gabriela - Editor

    helena = User.query.get(54)
    helena.job_titles.append(editor) # Helena - Editor
    helena.job_titles.append(assistant_editor) # Helena - Assistant Editor

    isabella = User.query.get(55)
    isabella.job_titles.append(editor) # Isabella - Editor

    juana = User.query.get(56)
    juana.job_titles.append(editor) # Juana - Editor
    juana.job_titles.append(assistant_editor) # Juana - Assistant Editor

    karla = User.query.get(57)
    karla.job_titles.append(editor) # Karla - Editor

    lucia = User.query.get(58)
    lucia.job_titles.append(editor) # Lucia - Editor
    lucia.job_titles.append(assistant_editor) # Lucia - Assistant Editor

    mariana = User.query.get(59)
    mariana.job_titles.append(editor) # Mariana - Editor

    natalia = User.query.get(60)
    natalia.job_titles.append(editor) # Natalia - Editor
    natalia.job_titles.append(assistant_editor) # Natalia - Assistant Editor

    olivia = User.query.get(61)
    olivia.job_titles.append(editor) # Olivia - Editor

    penelope = User.query.get(62)
    penelope.job_titles.append(editor) # Penelope - Editor
    penelope.job_titles.append(assistant_editor) # Penelope - Assistant Editor

    quinn = User.query.get(63)
    quinn.job_titles.append(editor) # Quinn - Editor

    rachel = User.query.get(64)
    rachel.job_titles.append(editor) # Rachel - Editor
    rachel.job_titles.append(assistant_editor) # Rachel - Assistant Editor

    sophia = User.query.get(65)
    sophia.job_titles.append(editor) # Sophia - Editor

    tiffany = User.query.get(66)
    tiffany.job_titles.append(editor) # Tiffany - Editor
    tiffany.job_titles.append(assistant_editor) # Tiffany - Assistant Editor

    ursula = User.query.get(67)
    ursula.job_titles.append(editor) # Ursula - Editor

    victoria = User.query.get(68)
    victoria.job_titles.append(editor) # Victoria - Editor
    victoria.job_titles.append(assistant_editor) # Victoria - Assistant Editor

    wendy = User.query.get(69)
    wendy.job_titles.append(editor) # Wendy - Editor

    xena = User.query.get(70)
    xena.job_titles.append(editor) # Xena - Editor
    xena.job_titles.append(assistant_editor) # Xena - Assistant Editor

    aaron = User.query.get(71)
    aaron.job_titles.append(editor) # Aaron - Editor

    brian = User.query.get(72)
    brian.job_titles.append(editor) # Brian - Editor
    brian.job_titles.append(assistant_editor) # Brian - Assistant Editor

    cameron = User.query.get(73)
    cameron.job_titles.append(editor) # Cameron - Editor

    dylan = User.query.get(74)
    dylan.job_titles.append(editor) # Dylan - Editor
    dylan.job_titles.append(assistant_editor) # Dylan - Assistant Editor

    ethan = User.query.get(75)
    ethan.job_titles.append(editor) # Ethan - Editor

    felix = User.query.get(76)
    felix.job_titles.append(editor) # Felix - Editor
    felix.job_titles.append(assistant_editor) # Felix - Assistant Editor

    gavin = User.query.get(77)
    gavin.job_titles.append(editor) # Gavin - Editor

    henry = User.query.get(78)
    henry.job_titles.append(editor) # Henry - Editor
    henry.job_titles.append(assistant_editor) # Henry - Assistant Editor

    ian = User.query.get(79)
    ian.job_titles.append(editor) # Ian - Editor

    jack = User.query.get(80)
    jack.job_titles.append(editor) # Jack - Editor
    jack.job_titles.append(assistant_editor) # Jack - Assistant Editor


    kamila = User.query.get(81)
    kamila.job_titles.append(editor) # Kamila - Editor

    laila = User.query.get(82)
    laila.job_titles.append(editor) # Laila - Editor
    laila.job_titles.append(assistant_editor) # Laila - Assistant Editor

    maha = User.query.get(83)
    maha.job_titles.append(editor) # Maha - Editor

    nadia = User.query.get(84)
    nadia.job_titles.append(editor) # Nadia - Editor
    nadia.job_titles.append(assistant_editor) # Nadia - Assistant Editor

    omarah = User.query.get(85)
    omarah.job_titles.append(editor) # Omarah - Editor

    pari = User.query.get(86)
    pari.job_titles.append(editor) # Pari - Editor
    pari.job_titles.append(assistant_editor) # Pari - Assistant Editor

    qadira = User.query.get(87)
    qadira.job_titles.append(editor) # Qadira - Editor

    rana = User.query.get(88)
    rana.job_titles.append(editor) # Rana - Editor
    rana.job_titles.append(assistant_editor) # Rana - Assistant Editor

    sahar = User.query.get(89)
    sahar.job_titles.append(editor) # Sahar - Editor

    tahira = User.query.get(90)
    tahira.job_titles.append(editor) # Tahira - Editor
    tahira.job_titles.append(assistant_editor) # Tahira - Assistant Editor

    uma = User.query.get(91)
    uma.job_titles.append(editor) # Uma - Editor

    valentina = User.query.get(92)
    valentina.job_titles.append(editor) # Valentina - Editor
    valentina.job_titles.append(assistant_editor) # Valentina - Assistant Editor

    waleed = User.query.get(93)
    waleed.job_titles.append(editor) # Waleed - Editor

    xia = User.query.get(94)
    xia.job_titles.append(editor) # Xia - Editor
    xia.job_titles.append(assistant_editor) # Xia -

    yusuf = User.query.get(95)
    yusuf.job_titles.append(editor) # Yusuf - Editor

    zahra = User.query.get(96)
    zahra.job_titles.append(editor) # Zahra - Editor
    zahra.job_titles.append(assistant_editor) # Zahra - Assistant Editor

    amos = User.query.get(97)
    amos.job_titles.append(editor) # Amos - Editor

    brittany = User.query.get(98)
    brittany.job_titles.append(editor) # Brittany - Editor
    brittany.job_titles.append(assistant_editor) # Brittany - Assistant Editor

    carlos = User.query.get(99)
    carlos.job_titles.append(editor) # Carlos - Editor

    diana = User.query.get(100)
    diana.job_titles.append(editor) # Diana - Editor
    diana.job_titles.append(assistant_editor) # Diana - Assistant Editor
    
    
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
