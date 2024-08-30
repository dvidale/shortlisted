from app.models import db,  environment, SCHEMA, User, Job_Title
from app.models import user_job_title


from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_user_job_titles():
   
    editor = Job_Title.query.get(1)
    assistant_editor = Job_Title.query.get(2)

    
    aaliyah = User.query.get(1),
    brianna = User.query.get(2),
    ciara = User.query.get(3),
    deja = User.query.get(4),
    emani = User.query.get(5),
    faith = User.query.get(6),
    gabrielle = User.query.get(7),
    halle = User.query.get(8),
    imani = User.query.get(9),
    jada = User.query.get(10),
    
    aaron = User.query.get(11),
    brandon = User.query.get(12),
    caleb = User.query.get(13),
    darius = User.query.get(14),
    elijah = User.query.get(15),
    franklin = User.query.get(16),
    gregory = User.query.get(17),
    howard = User.query.get(18),
    isaiah = User.query.get(19),
    jason = User.query.get(20),
    
    arjun = User.query.get(21),
    bilal = User.query.get(22),
    chetan = User.query.get(23),
    dev = User.query.get(24),
    eshan = User.query.get(25),
    faisal = User.query.get(26),
    gautam = User.query.get(27),
    harish = User.query.get(28),
    imran = User.query.get(29),
    jai = User.query.get(30),
    
    kavya = User.query.get(31),
    lata = User.query.get(32),
    meera = User.query.get(33),
    naina = User.query.get(34),
    oorja = User.query.get(35),
    pooja = User.query.get(36),
    qadira = User.query.get(37),
    rani = User.query.get(38),
    sanya = User.query.get(39),
    tanvi = User.query.get(40),
    
    elena = User.query.get(41),
    frida = User.query.get(42),
    gabriela = User.query.get(43),
    helena = User.query.get(44),
    isabella = User.query.get(45),
    juana = User.query.get(46),
    karla = User.query.get(47),
    lucia = User.query.get(48),
    mariana = User.query.get(49),
    natalia = User.query.get(50),
    
    olivia = User.query.get(51),
    penelope = User.query.get(52),
    quinn = User.query.get(53),
    rachel = User.query.get(54),
    sophia = User.query.get(55),
    tiffany = User.query.get(56),
    ursula = User.query.get(57),
    victoria = User.query.get(58),
    wendy = User.query.get(59),
    xena = User.query.get(60),
    
    aaron = User.query.get(61),
    brian = User.query.get(62),
    cameron = User.query.get(63),
    dylan = User.query.get(64),
    ethan = User.query.get(65),
    felix = User.query.get(66),
    gavin = User.query.get(67),
    henry = User.query.get(68),
    ian = User.query.get(69),
    jack = User.query.get(70),
    
    karim = User.query.get(71),
    laila = User.query.get(72),
    mona = User.query.get(73),
    nadia = User.query.get(74),
    omar = User.query.get(75),
    parvin = User.query.get(76),
    qasim = User.query.get(77),
    rasha = User.query.get(78),
    samira = User.query.get(79),
    tariq = User.query.get(80),
    
    umar = User.query.get(81),
    yasmin = User.query.get(82),
    zara = User.query.get(83),
    ahmad = User.query.get(84),
    bushra = User.query.get(85),
    deen = User.query.get(86),
    eman = User.query.get(87),
    fatima = User.query.get(88),
    ghada = User.query.get(89),
    hamed = User.query.get(90),
    
    isra = User.query.get(91),
    jamal = User.query.get(92),
    khalid = User.query.get(93),
    leila = User.query.get(94),
    mustafa = User.query.get(95),
    noura = User.query.get(96),
    omar = User.query.get(97),
    reem = User.query.get(98),
    salim = User.query.get(99),
    wafa = User.query.get(100),


    aaliyah.to_dict().job_titles.append(editor)  # Aaliyah - Editor
    aaliyah.to_dict().job_titles.append(assistant_editor)  # Aaliyah - Assistant Editor

    brianna.to_dict().job_titles.append(editor)  # Brianna - Editor
    brianna.to_dict().job_titles.append(assistant_editor)  # Brianna - Assistant Editor

    ciara.to_dict().job_titles.append(editor)  # Ciara - Editor
    ciara.to_dict().job_titles.append(assistant_editor)  # Ciara - Assistant Editor

    deja.to_dict().job_titles.append(editor)  # Deja - Editor
    deja.to_dict().job_titles.append(assistant_editor)  # Deja - Assistant Editor

    emani.to_dict().job_titles.append(editor)  # Emani - Editor
    emani.to_dict().job_titles.append(assistant_editor)  # Emani - Assistant Editor

    faith.to_dict().job_titles.append(editor)  # Faith - Editor
    faith.to_dict().job_titles.append(assistant_editor)  # Faith - Assistant Editor

    gabrielle.to_dict().job_titles.append(editor)  # Gabrielle - Editor
    gabrielle.to_dict().job_titles.append(assistant_editor)  # Gabrielle - Assistant Editor

    halle.to_dict().job_titles.append(editor)  # Halle - Editor
    halle.to_dict().job_titles.append(assistant_editor)  # Halle - Assistant Editor

    imani.to_dict().job_titles.append(editor)  # Imani - Editor
    imani.to_dict().job_titles.append(assistant_editor)  # Imani - Assistant Editor

    jada.to_dict().job_titles.append(editor)  # Jada - Editor
    jada.to_dict().job_titles.append(assistant_editor)  # Jada - Assistant Editor

    aaron.to_dict().job_titles.append(editor)  # Aaron - Editor
    aaron.to_dict().job_titles.append(assistant_editor)  # Aaron - Assistant Editor

    brandon.to_dict().job_titles.append(editor)  # Brandon - Editor
    brandon.to_dict().job_titles.append(assistant_editor)  # Brandon - Assistant Editor

    caleb.to_dict().job_titles.append(editor)  # Caleb - Editor
    caleb.to_dict().job_titles.append(assistant_editor)  # Caleb - Assistant Editor

    darius.to_dict().job_titles.append(editor)  # Darius - Editor
    darius.to_dict().job_titles.append(assistant_editor)  # Darius - Assistant Editor

    elijah.to_dict().job_titles.append(editor)  # Elijah - Editor
    elijah.to_dict().job_titles.append(assistant_editor)  # Elijah - Assistant Editor

    franklin.to_dict().job_titles.append(editor)  # Franklin - Editor
    franklin.to_dict().job_titles.append(assistant_editor)  # Franklin - Assistant Editor

    gregory.to_dict().job_titles.append(editor)  # Gregory - Editor
    gregory.to_dict().job_titles.append(assistant_editor)  # Gregory - Assistant Editor

    howard.to_dict().job_titles.append(editor)  # Howard - Editor
    howard.to_dict().job_titles.append(assistant_editor)  # Howard - Assistant Editor

    isaiah.to_dict().job_titles.append(editor)  # Isaiah - Editor
    isaiah.to_dict().job_titles.append(assistant_editor)  # Isaiah - Assistant Editor

    jason.to_dict().job_titles.append(editor)  # Jason - Editor
    jason.to_dict().job_titles.append(assistant_editor)  # Jason - Assistant Editor

    arjun.to_dict().job_titles.append(editor)  # Arjun - Editor
    arjun.to_dict().job_titles.append(assistant_editor)  # Arjun - Assistant Editor

    bilal.to_dict().job_titles.append(editor)  # Bilal - Editor
    bilal.to_dict().job_titles.append(assistant_editor)  # Bilal - Assistant Editor

    chetan.to_dict().job_titles.append(editor)  # Chetan - Editor
    chetan.to_dict().job_titles.append(assistant_editor)  # Chetan - Assistant Editor

    dev.to_dict().job_titles.append(editor)  # Dev - Editor
    dev.to_dict().job_titles.append(assistant_editor)  # Dev - Assistant Editor

    eshan.to_dict().job_titles.append(editor)  # Eshan - Editor
    eshan.to_dict().job_titles.append(assistant_editor)  # Eshan - Assistant Editor

    faisal.to_dict().job_titles.append(editor)  # Faisal - Editor
    faisal.to_dict().job_titles.append(assistant_editor)  # Faisal - Assistant Editor

    gautam.to_dict().job_titles.append(editor)  # Gautam - Editor
    gautam.to_dict().job_titles.append(assistant_editor)  # Gautam - Assistant Editor

    harish.to_dict().job_titles.append(editor)  # Harish - Editor
    harish.to_dict().job_titles.append(assistant_editor)  # Harish - Assistant Editor

    imran.to_dict().job_titles.append(editor)  # Imran - Editor
    imran.to_dict().job_titles.append(assistant_editor)  # Imran - Assistant Editor

    jai.to_dict().job_titles.append(editor)  # Jai - Editor
    jai.to_dict().job_titles.append(assistant_editor)  # Jai - Assistant Editor

    kavya.to_dict().job_titles.append(editor)  # Kavya - Editor
    kavya.to_dict().job_titles.append(assistant_editor)  # Kavya - Assistant Editor

    lata.to_dict().job_titles.append(editor)  # Lata - Editor
    lata.to_dict().job_titles.append(assistant_editor)  # Lata - Assistant Editor

    meera.to_dict().job_titles.append(editor)  # Meera - Editor
    meera.to_dict().job_titles.append(assistant_editor)  # Meera - Assistant Editor

    naina.to_dict().job_titles.append(editor)  # Naina - Editor
    naina.to_dict().job_titles.append(assistant_editor)  # Naina - Assistant Editor

    oorja.to_dict().job_titles.append(editor)  # Oorja - Editor
    oorja.to_dict().job_titles.append(assistant_editor)  # Oorja - Assistant Editor

    pooja.to_dict().job_titles.append(editor)  # Pooja - Editor
    pooja.to_dict().job_titles.append(assistant_editor)  # Pooja - Assistant Editor

    qadira.to_dict().job_titles.append(editor)  # Qadira - Editor
    qadira.to_dict().job_titles.append(assistant_editor)  # Qadira - Assistant Editor

    rani.to_dict().job_titles.append(editor)  # Rani - Editor
    rani.to_dict().job_titles.append(assistant_editor)  # Rani - Assistant Editor

    sanya.to_dict().job_titles.append(editor)  # Sanya - Editor
    sanya.to_dict().job_titles.append(assistant_editor)  # Sanya - Assistant Editor

    tanvi.to_dict().job_titles.append(editor)  # Tanvi - Editor
    tanvi.to_dict().job_titles.append(assistant_editor)  # Tanvi - Assistant Editor

    elena.to_dict().job_titles.append(editor)  # Elena - Editor
    elena.to_dict().job_titles.append(assistant_editor)  # Elena - Assistant Editor

    frida.to_dict().job_titles.append(editor)  # Frida - Editor
    frida.to_dict().job_titles.append(assistant_editor)  # Frida - Assistant Editor

    gabriela.to_dict().job_titles.append(editor)  # Gabriela - Editor
    gabriela.to_dict().job_titles.append(assistant_editor)  # Gabriela - Assistant Editor

    helena.to_dict().job_titles.append(editor)  # Helena - Editor
    helena.to_dict().job_titles.append(assistant_editor)  # Helena - Assistant Editor

    isabella.to_dict().job_titles.append(editor)  # Isabella - Editor
    isabella.to_dict().job_titles.append(assistant_editor)  # Isabella - Assistant Editor

    juana.to_dict().job_titles.append(editor)  # Juana - Editor
    juana.to_dict().job_titles.append(assistant_editor)  # Juana - Assistant Editor

    karla.to_dict().job_titles.append(editor)  # Karla - Editor
    karla.to_dict().job_titles.append(assistant_editor)  # Karla - Assistant Editor

    lucia.to_dict().job_titles.append(editor)  # Lucia - Editor
    lucia.to_dict().job_titles.append(assistant_editor)  # Lucia - Assistant Editor

    mariana.to_dict().job_titles.append(editor)  # Mariana - Editor
    mariana.to_dict().job_titles.append(assistant_editor)  # Mariana - Assistant Editor

    natalia.to_dict().job_titles.append(editor)  # Natalia - Editor
    natalia.to_dict().job_titles.append(assistant_editor)  # Natalia - Assistant Editor

    olivia.to_dict().job_titles.append(editor)  # Olivia - Editor
    olivia.to_dict().job_titles.append(assistant_editor)  # Olivia - Assistant Editor

    penelope.to_dict().job_titles.append(editor)  # Penelope - Editor
    penelope.to_dict().job_titles.append(assistant_editor)  # Penelope - Assistant Editor

    quinn.to_dict().job_titles.append(editor)  # Quinn - Editor
    quinn.to_dict().job_titles.append(assistant_editor)  # Quinn - Assistant Editor

    rachel.to_dict().job_titles.append(editor)  # Rachel - Editor
    rachel.to_dict().job_titles.append(assistant_editor)  # Rachel - Assistant Editor

    sophia.to_dict().job_titles.append(editor)  # Sophia - Editor
    sophia.to_dict().job_titles.append(assistant_editor)  # Sophia - Assistant Editor

    tiffany.to_dict().job_titles.append(editor)  # Tiffany - Editor
    tiffany.to_dict().job_titles.append(assistant_editor)  # Tiffany - Assistant Editor

    ursula.to_dict().job_titles.append(editor)  # Ursula - Editor
    ursula.to_dict().job_titles.append(assistant_editor)  # Ursula - Assistant Editor

    victoria.to_dict().job_titles.append(editor)  # Victoria - Editor
    victoria.to_dict().job_titles.append(assistant_editor)  # Victoria - Assistant Editor

    wendy.to_dict().job_titles.append(editor)  # Wendy - Editor
    wendy.to_dict().job_titles.append(assistant_editor)  # Wendy - Assistant Editor

    xena.to_dict().job_titles.append(editor)  # Xena - Editor
    xena.to_dict().job_titles.append(assistant_editor)  # Xena - Assistant Editor

    aaron.to_dict().job_titles.append(editor)  # Aaron - Editor
    aaron.to_dict().job_titles.append(assistant_editor)  # Aaron - Assistant Editor

    brian.to_dict().job_titles.append(editor)  # Brian - Editor
    brian.to_dict().job_titles.append(assistant_editor)  # Brian - Assistant Editor

    cameron.to_dict().job_titles.append(editor)  # Cameron - Editor
    cameron.to_dict().job_titles.append(assistant_editor)  # Cameron - Assistant Editor

    dylan.to_dict().job_titles.append(editor)  # Dylan - Editor
    dylan.to_dict().job_titles.append(assistant_editor)  # Dylan - Assistant Editor

    ethan.to_dict().job_titles.append(editor)  # Ethan - Editor
    ethan.to_dict().job_titles.append(assistant_editor)  # Ethan - Assistant Editor

    felix.to_dict().job_titles.append(editor)  # Felix - Editor
    felix.to_dict().job_titles.append(assistant_editor)  # Felix - Assistant Editor

    gavin.to_dict().job_titles.append(editor)  # Gavin - Editor
    gavin.to_dict().job_titles.append(assistant_editor)  # Gavin - Assistant Editor

    henry.to_dict().job_titles.append(editor)  # Henry - Editor
    henry.to_dict().job_titles.append(assistant_editor)  # Henry - Assistant Editor

    ian.to_dict().job_titles.append(editor)  # Ian - Editor
    ian.to_dict().job_titles.append(assistant_editor)  # Ian - Assistant Editor

    jack.to_dict().job_titles.append(editor)  # Jack - Editor
    jack.to_dict().job_titles.append(assistant_editor)  # Jack - Assistant Editor

    karim.to_dict().job_titles.append(editor)  # Karim - Editor
    karim.to_dict().job_titles.append(assistant_editor)  # Karim - Assistant Editor

    laila.to_dict().job_titles.append(editor)  # Laila - Editor
    laila.to_dict().job_titles.append(assistant_editor)  # Laila - Assistant Editor

    mona.to_dict().job_titles.append(editor)  # Mona - Editor
    mona.to_dict().job_titles.append(assistant_editor)  # Mona - Assistant Editor

    nadia.to_dict().job_titles.append(editor)  # Nadia - Editor
    nadia.to_dict().job_titles.append(assistant_editor)  # Nadia - Assistant Editor

    omar.to_dict().job_titles.append(editor)  # Omar - Editor
    omar.to_dict().job_titles.append(assistant_editor)  # Omar - Assistant Editor

    parvin.to_dict().job_titles.append(editor)  # Parvin - Editor
    parvin.to_dict().job_titles.append(assistant_editor)  # Parvin - Assistant Editor

    qasim.to_dict().job_titles.append(editor)  # Qasim - Editor
    qasim.to_dict().job_titles.append(assistant_editor)  # Qasim - Assistant Editor

    rasha.to_dict().job_titles.append(editor)  # Rasha - Editor
    rasha.to_dict().job_titles.append(assistant_editor)  # Rasha - Assistant Editor

    samira.to_dict().job_titles.append(editor)  # Samira - Editor
    samira.to_dict().job_titles.append(assistant_editor)  # Samira - Assistant Editor

    tariq.to_dict().job_titles.append(editor)  # Tariq - Editor
    tariq.to_dict().job_titles.append(assistant_editor)  # Tariq - Assistant Editor

    umar.to_dict().job_titles.append(editor)  # Umar - Editor
    umar.to_dict().job_titles.append(assistant_editor)  # Umar - Assistant Editor

    yasmin.to_dict().job_titles.append(editor)  # Yasmin - Editor
    yasmin.to_dict().job_titles.append(assistant_editor)  # Yasmin - Assistant Editor

    zara.to_dict().job_titles.append(editor)  # Zara - Editor
    zara.to_dict().job_titles.append(assistant_editor)  # Zara - Assistant Editor

    ahmad.to_dict().job_titles.append(editor)  # Ahmad - Editor
    ahmad.to_dict().job_titles.append(assistant_editor)  # Ahmad - Assistant Editor

    bushra.to_dict().job_titles.append(editor)  # Bushra - Editor
    bushra.to_dict().job_titles.append(assistant_editor)  # Bushra - Assistant Editor

    deen.to_dict().job_titles.append(editor)  # Deen - Editor
    deen.to_dict().job_titles.append(assistant_editor)  # Deen - Assistant Editor

    eman.to_dict().job_titles.append(editor)  # Eman - Editor
    eman.to_dict().job_titles.append(assistant_editor)  # Eman - Assistant Editor

    fatima.to_dict().job_titles.append(editor)  # Fatima - Editor
    fatima.to_dict().job_titles.append(assistant_editor)  # Fatima - Assistant Editor

    ghada.to_dict().job_titles.append(editor)  # Ghada - Editor
    ghada.to_dict().job_titles.append(assistant_editor)  # Ghada - Assistant Editor

    hamed.to_dict().job_titles.append(editor)  # Hamed - Editor
    hamed.to_dict().job_titles.append(assistant_editor)  # Hamed - Assistant Editor

    isra.to_dict().job_titles.append(editor)  # Isra - Editor
    isra.to_dict().job_titles.append(assistant_editor)  # Isra - Assistant Editor

    jamal.to_dict().job_titles.append(editor)  # Jamal - Editor
    jamal.to_dict().job_titles.append(assistant_editor)  # Jamal - Assistant Editor

    khalid.to_dict().job_titles.append(editor)  # Khalid - Editor
    khalid.to_dict().job_titles.append(assistant_editor)  # Khalid - Assistant Editor

    leila.to_dict().job_titles.append(editor)  # Leila - Editor
    leila.to_dict().job_titles.append(assistant_editor)  # Leila - Assistant Editor

    mustafa.to_dict().job_titles.append(editor)  # Mustafa - Editor
    mustafa.to_dict().job_titles.append(assistant_editor)  # Mustafa - Assistant Editor

    noura.to_dict().job_titles.append(editor)  # Noura - Editor
    noura.to_dict().job_titles.append(assistant_editor)  # Noura - Assistant Editor

    omar.to_dict().job_titles.append(editor)  # Omar - Editor
    omar.to_dict().job_titles.append(assistant_editor)  # Omar - Assistant Editor

    reem.to_dict().job_titles.append(editor)  # Reem - Editor
    reem.to_dict().job_titles.append(assistant_editor)  # Reem - Assistant Editor

    salim.to_dict().job_titles.append(editor)  # Salim - Editor
    salim.to_dict().job_titles.append(assistant_editor)  # Salim - Assistant Editor

    wafa.to_dict().job_titles.append(editor)  # Wafa - Editor
    wafa.to_dict().job_titles.append(assistant_editor)  # Wafa - Assistant Editor

        
    
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
