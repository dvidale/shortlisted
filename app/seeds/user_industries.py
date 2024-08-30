from app.models import db, environment, SCHEMA, User, Industry_Area

from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_user_industries():
    # Fetch users and industry areas from the database
    # African American Women
    aaliyah = User.query.get(1)
    imani = User.query.get(2)
    kaiya = User.query.get(3)
    makayla = User.query.get(4)
    zuri = User.query.get(5)
    sanaa = User.query.get(6)
    nala = User.query.get(7)
    ariyah = User.query.get(8)
    amara = User.query.get(9)
    jaleah = User.query.get(10)

    # African American Men
    elijah = User.query.get(11)
    xavier = User.query.get(12)
    malik = User.query.get(13)
    tyrone = User.query.get(14)
    amir = User.query.get(15)
    darius = User.query.get(16)
    jamal = User.query.get(17)
    khalil = User.query.get(18)
    nasir = User.query.get(19)
    quincy = User.query.get(20)

    # South Asian Men
    rahul = User.query.get(21)
    arjun = User.query.get(22)
    sanjay = User.query.get(23)
    vikram = User.query.get(24)
    amit = User.query.get(25)
    deepak = User.query.get(26)
    raj = User.query.get(27)
    ravi = User.query.get(28)
    harsh = User.query.get(29)
    manish = User.query.get(30)

    # South Asian Women
    anika = User.query.get(31)
    isha = User.query.get(32)
    padmini = User.query.get(33)
    maya = User.query.get(34)
    kavita = User.query.get(35)
    neha = User.query.get(36)
    rani = User.query.get(37)
    divya = User.query.get(38)
    lakshmi = User.query.get(39)
    tara = User.query.get(40)

    # Hispanic Men
    alejandro = User.query.get(41)
    carlos = User.query.get(42)
    diego = User.query.get(43)
    emilio = User.query.get(44)
    fernando = User.query.get(45)
    hector = User.query.get(46)
    javier = User.query.get(47)
    luis = User.query.get(48)
    miguel = User.query.get(49)
    ricardo = User.query.get(50)

    # Hispanic Women
    ana = User.query.get(51)
    bianca = User.query.get(52)
    carla = User.query.get(53)
    elena = User.query.get(54)
    gabriela = User.query.get(55)
    isabel = User.query.get(56)
    luz = User.query.get(57)
    maria = User.query.get(58)
    natalia = User.query.get(59)
    sofia = User.query.get(60)

    # White Men
    andrew = User.query.get(61)
    brian = User.query.get(62)
    charles = User.query.get(63)
    david = User.query.get(64)
    edward = User.query.get(65)
    frank = User.query.get(66)
    george = User.query.get(67)
    henry = User.query.get(68)
    ian = User.query.get(69)
    john = User.query.get(70)

    # White Women
    alice = User.query.get(71)
    beth = User.query.get(72)
    claire = User.query.get(73)
    diana = User.query.get(74)
    emily = User.query.get(75)
    fiona = User.query.get(76)
    grace = User.query.get(77)
    helen = User.query.get(78)
    iris = User.query.get(79)
    julia = User.query.get(80)

    # Middle Eastern Men
    ahmad = User.query.get(81)
    basim = User.query.get(82)
    farid = User.query.get(83)
    hadi = User.query.get(84)
    jamal_m = User.query.get(85)
    karim = User.query.get(86)
    nabil = User.query.get(87)
    omar = User.query.get(88)
    rami = User.query.get(89)
    yasin = User.query.get(90)

    # Middle Eastern Women
    amina_f = User.query.get(91)
    dalal = User.query.get(92)
    farah = User.query.get(93)
    hana = User.query.get(94)
    iman = User.query.get(95)
    lina = User.query.get(96)
    mariam = User.query.get(97)
    nadia = User.query.get(98)
    rima = User.query.get(99)
    yasmin = User.query.get(100)


    scripted_television = Industry_Area.query.get(1)
    unscripted_television = Industry_Area.query.get(2)
    dramatic_film = Industry_Area.query.get(3)
    documentary = Industry_Area.query.get(4)
    commercial = Industry_Area.query.get(5)
    animation = Industry_Area.query.get(6)


    # Associate industry areas with users
    # African American Women
    aaliyah.industry_areas.append(scripted_television)  # Amina - Scripted Television
    aaliyah.industry_areas.append(documentary)  # Amina - Documentary

    imani.industry_areas.append(dramatic_film)  # Imani - Dramatic Film
    imani.industry_areas.append(animation)  # Imani - Animation

    kaiya.industry_areas.append(commercial)  # Kaiya - Commercial
    kaiya.industry_areas.append(documentary)  # Kaiya - Documentary

    makayla.industry_areas.append(scripted_television)  # Makayla - Scripted Television
    makayla.industry_areas.append(dramatic_film)  # Makayla - Dramatic Film

    zuri.industry_areas.append(animation)  # Zuri - Animation
    zuri.industry_areas.append(commercial)  # Zuri - Commercial

    sanaa.industry_areas.append(unscripted_television)  # Sanaa - Unscripted Television
    sanaa.industry_areas.append(documentary)  # Sanaa - Documentary

    nala.industry_areas.append(scripted_television)  # Nala - Scripted Television
    nala.industry_areas.append(animation)  # Nala - Animation

    ariyah.industry_areas.append(dramatic_film)  # Ariyah - Dramatic Film
    ariyah.industry_areas.append(unscripted_television)  # Ariyah - Unscripted Television

    amara.industry_areas.append(commercial)  # Amara - Commercial
    amara.industry_areas.append(documentary)  # Amara - Documentary

    jaleah.industry_areas.append(scripted_television)  # Jaleah - Scripted Television
    jaleah.industry_areas.append(dramatic_film)  # Jaleah - Dramatic Film

    # African American Men
    elijah.industry_areas.append(unscripted_television)  # Elijah - Unscripted Television
    elijah.industry_areas.append(animation)  # Elijah - Animation

    xavier.industry_areas.append(scripted_television)  # Xavier - Scripted Television
    xavier.industry_areas.append(documentary)  # Xavier - Documentary

    malik.industry_areas.append(dramatic_film)  # Malik - Dramatic Film
    malik.industry_areas.append(commercial)  # Malik - Commercial

    tyrone.industry_areas.append(animation)  # Tyrone - Animation
    tyrone.industry_areas.append(documentary)  # Tyrone - Documentary

    amir.industry_areas.append(unscripted_television)  # Amir - Unscripted Television
    amir.industry_areas.append(scripted_television)  # Amir - Scripted Television

    darius.industry_areas.append(dramatic_film)  # Darius - Dramatic Film
    darius.industry_areas.append(documentary)  # Darius - Documentary

    jamal.industry_areas.append(commercial)  # Jamal - Commercial
    jamal.industry_areas.append(unscripted_television)  # Jamal - Unscripted Television

    khalil.industry_areas.append(animation)  # Khalil - Animation
    khalil.industry_areas.append(scripted_television)  # Khalil - Scripted Television

    nasir.industry_areas.append(dramatic_film)  # Nasir - Dramatic Film
    nasir.industry_areas.append(commercial)  # Nasir - Commercial

    quincy.industry_areas.append(documentary)  # Quincy - Documentary
    quincy.industry_areas.append(scripted_television)  # Quincy - Scripted Television

    # South Asian Men
    rahul.industry_areas.append(scripted_television)  # Rahul - Scripted Television
    rahul.industry_areas.append(dramatic_film)  # Rahul - Dramatic Film

    arjun.industry_areas.append(animation)  # Arjun - Animation
    arjun.industry_areas.append(unscripted_television)  # Arjun - Unscripted Television

    sanjay.industry_areas.append(commercial)  # Sanjay - Commercial
    sanjay.industry_areas.append(documentary)  # Sanjay - Documentary

    vikram.industry_areas.append(unscripted_television)  # Vikram - Unscripted Television
    vikram.industry_areas.append(scripted_television)  # Vikram - Scripted Television

    amit.industry_areas.append(dramatic_film)  # Amit - Dramatic Film
    amit.industry_areas.append(animation)  # Amit - Animation

    deepak.industry_areas.append(scripted_television)  # Deepak - Scripted Television
    deepak.industry_areas.append(documentary)  # Deepak - Documentary

    raj.industry_areas.append(commercial)  # Raj - Commercial
    raj.industry_areas.append(unscripted_television)  # Raj - Unscripted Television

    ravi.industry_areas.append(animation)  # Ravi - Animation
    ravi.industry_areas.append(scripted_television)  # Ravi - Scripted Television

    harsh.industry_areas.append(dramatic_film)  # Harsh - Dramatic Film
    harsh.industry_areas.append(commercial)  # Harsh - Commercial

    manish.industry_areas.append(documentary)  # Manish - Documentary
    manish.industry_areas.append(scripted_television)  # Manish - Scripted Television

    # South Asian Women
    anika.industry_areas.append(scripted_television)  # Anika - Scripted Television
    anika.industry_areas.append(documentary)  # Anika - Documentary

    isha.industry_areas.append(dramatic_film)  # Isha - Dramatic Film
    isha.industry_areas.append(animation)  # Isha - Animation

    padmini.industry_areas.append(commercial)  # Padmini - Commercial
    padmini.industry_areas.append(documentary)  # Padmini - Documentary

    maya.industry_areas.append(scripted_television)  # Maya - Scripted Television
    maya.industry_areas.append(dramatic_film)  # Maya - Dramatic Film

    kavita.industry_areas.append(animation)  # Kavita - Animation
    kavita.industry_areas.append(commercial)  # Kavita - Commercial

    neha.industry_areas.append(unscripted_television)  # Neha - Unscripted Television
    neha.industry_areas.append(documentary)  # Neha - Documentary

    rani.industry_areas.append(scripted_television)  # Rani - Scripted Television
    rani.industry_areas.append(animation)  # Rani - Animation

    divya.industry_areas.append(dramatic_film)  # Divya - Dramatic Film
    divya.industry_areas.append(unscripted_television)  # Divya - Unscripted Television

    lakshmi.industry_areas.append(commercial)  # Lakshmi - Commercial
    lakshmi.industry_areas.append(documentary)  # Lakshmi - Documentary

    tara.industry_areas.append(scripted_television)  # Tara - Scripted Television
    tara.industry_areas.append(dramatic_film)  # Tara - Dramatic Film

    # Hispanic Men
    alejandro.industry_areas.append(unscripted_television)  # Alejandro - Unscripted Television
    alejandro.industry_areas.append(animation)  # Alejandro - Animation

    carlos.industry_areas.append(scripted_television)  # Carlos - Scripted Television
    carlos.industry_areas.append(documentary)  # Carlos - Documentary

    diego.industry_areas.append(dramatic_film)  # Diego - Dramatic Film
    diego.industry_areas.append(commercial)  # Diego - Commercial

    emilio.industry_areas.append(animation)  # Emilio - Animation
    emilio.industry_areas.append(documentary)  # Emilio - Documentary

    fernando.industry_areas.append(unscripted_television)  # Fernando - Unscripted Television
    fernando.industry_areas.append(scripted_television)  # Fernando - Scripted Television

    hector.industry_areas.append(dramatic_film)  # Hector - Dramatic Film
    hector.industry_areas.append(documentary)  # Hector - Documentary

    javier.industry_areas.append(commercial)  # Javier - Commercial
    javier.industry_areas.append(unscripted_television)  # Javier - Unscripted Television

    luis.industry_areas.append(animation)  # Luis - Animation
    luis.industry_areas.append(scripted_television)  # Luis - Scripted Television

    miguel.industry_areas.append(dramatic_film)  # Miguel - Dramatic Film
    miguel.industry_areas.append(commercial)  # Miguel - Commercial

    ricardo.industry_areas.append(documentary)  # Ricardo - Documentary
    ricardo.industry_areas.append(scripted_television)  # Ricardo - Scripted Television

    # Hispanic Women
    ana.industry_areas.append(scripted_television)  # Ana - Scripted Television
    ana.industry_areas.append(documentary)  # Ana - Documentary

    bianca.industry_areas.append(dramatic_film)  # Bianca - Dramatic Film
    bianca.industry_areas.append(animation)

    # Hispanic Women
    ana.industry_areas.append(scripted_television)  # Ana - Scripted Television
    ana.industry_areas.append(documentary)  # Ana - Documentary

    bianca.industry_areas.append(dramatic_film)  # Bianca - Dramatic Film
    bianca.industry_areas.append(animation)  # Bianca - Animation

    carla.industry_areas.append(commercial)  # Carla - Commercial
    carla.industry_areas.append(documentary)  # Carla - Documentary

    elena.industry_areas.append(scripted_television)  # Elena - Scripted Television
    elena.industry_areas.append(dramatic_film)  # Elena - Dramatic Film

    gabriela.industry_areas.append(animation)  # Gabriela - Animation
    gabriela.industry_areas.append(commercial)  # Gabriela - Commercial

    isabel.industry_areas.append(unscripted_television)  # Isabel - Unscripted Television
    isabel.industry_areas.append(documentary)  # Isabel - Documentary

    luz.industry_areas.append(scripted_television)  # Luz - Scripted Television
    luz.industry_areas.append(animation)  # Luz - Animation

    maria.industry_areas.append(dramatic_film)  # Maria - Dramatic Film
    maria.industry_areas.append(unscripted_television)  # Maria - Unscripted Television

    natalia.industry_areas.append(commercial)  # Natalia - Commercial
    natalia.industry_areas.append(documentary)  # Natalia - Documentary

    sofia.industry_areas.append(scripted_television)  # Sofia - Scripted Television
    sofia.industry_areas.append(dramatic_film)  # Sofia - Dramatic Film

    # White Men
    andrew.industry_areas.append(unscripted_television)  # Andrew - Unscripted Television
    andrew.industry_areas.append(animation)  # Andrew - Animation

    brian.industry_areas.append(scripted_television)  # Brian - Scripted Television
    brian.industry_areas.append(documentary)  # Brian - Documentary

    charles.industry_areas.append(dramatic_film)  # Charles - Dramatic Film
    charles.industry_areas.append(commercial)  # Charles - Commercial

    david.industry_areas.append(animation)  # David - Animation
    david.industry_areas.append(documentary)  # David - Documentary

    edward.industry_areas.append(unscripted_television)  # Edward - Unscripted Television
    edward.industry_areas.append(scripted_television)  # Edward - Scripted Television

    frank.industry_areas.append(dramatic_film)  # Frank - Dramatic Film
    frank.industry_areas.append(documentary)  # Frank - Documentary

    george.industry_areas.append(commercial)  # George - Commercial
    george.industry_areas.append(unscripted_television)  # George - Unscripted Television

    henry.industry_areas.append(animation)  # Henry - Animation
    henry.industry_areas.append(scripted_television)  # Henry - Scripted Television

    ian.industry_areas.append(dramatic_film)  # Ian - Dramatic Film
    ian.industry_areas.append(commercial)  # Ian - Commercial

    john.industry_areas.append(documentary)  # John - Documentary
    john.industry_areas.append(scripted_television)  # John - Scripted Television

    # White Women
    alice.industry_areas.append(scripted_television)  # Alice - Scripted Television
    alice.industry_areas.append(documentary)  # Alice - Documentary

    beth.industry_areas.append(dramatic_film)  # Beth - Dramatic Film
    beth.industry_areas.append(animation)  # Beth - Animation

    claire.industry_areas.append(commercial)  # Claire - Commercial
    claire.industry_areas.append(documentary)  # Claire - Documentary

    diana.industry_areas.append(scripted_television)  # Diana - Scripted Television
    diana.industry_areas.append(dramatic_film)  # Diana - Dramatic Film

    emily.industry_areas.append(animation)  # Emily - Animation
    emily.industry_areas.append(commercial)  # Emily - Commercial

    fiona.industry_areas.append(unscripted_television)  # Fiona - Unscripted Television
    fiona.industry_areas.append(documentary)  # Fiona - Documentary

    grace.industry_areas.append(scripted_television)  # Grace - Scripted Television
    grace.industry_areas.append(animation)  # Grace - Animation

    helen.industry_areas.append(dramatic_film)  # Helen - Dramatic Film
    helen.industry_areas.append(unscripted_television)  # Helen - Unscripted Television

    iris.industry_areas.append(commercial)  # Iris - Commercial
    iris.industry_areas.append(documentary)  # Iris - Documentary

    julia.industry_areas.append(scripted_television)  # Julia - Scripted Television
    julia.industry_areas.append(dramatic_film)  # Julia - Dramatic Film

    # Middle Eastern Men
    ahmad.industry_areas.append(unscripted_television)  # Ahmad - Unscripted Television
    ahmad.industry_areas.append(animation)  # Ahmad - Animation

    basim.industry_areas.append(scripted_television)  # Basim - Scripted Television
    basim.industry_areas.append(documentary)  # Basim - Documentary

    farid.industry_areas.append(dramatic_film)  # Farid - Dramatic Film
    farid.industry_areas.append(commercial)  # Farid - Commercial

    hadi.industry_areas.append(animation)  # Hadi - Animation
    hadi.industry_areas.append(documentary)  # Hadi - Documentary

    jamal.industry_areas.append(unscripted_television)  # Jamal - Unscripted Television
    jamal.industry_areas.append(scripted_television)  # Jamal - Scripted Television

    karim.industry_areas.append(dramatic_film)  # Karim - Dramatic Film
    karim.industry_areas.append(documentary)  # Karim - Documentary

    nabil.industry_areas.append(commercial)  # Nabil - Commercial
    nabil.industry_areas.append(unscripted_television)  # Nabil - Unscripted Television

    omar.industry_areas.append(animation)  # Omar - Animation
    omar.industry_areas.append(scripted_television)  # Omar - Scripted Television

    rami.industry_areas.append(dramatic_film)  # Rami - Dramatic Film
    rami.industry_areas.append(commercial)  # Rami - Commercial

    yasin.industry_areas.append(documentary)  # Yasin - Documentary
    yasin.industry_areas.append(scripted_television)  # Yasin - Scripted Television

    # Middle Eastern Women
    amina_f.industry_areas.append(scripted_television)  # Amina - Scripted Television
    amina_f.industry_areas.append(documentary)  # Amina - Documentary

    dalal.industry_areas.append(dramatic_film)  # Dalal - Dramatic Film
    dalal.industry_areas.append(animation)  # Dalal - Animation

    farah.industry_areas.append(commercial)  # Farah - Commercial
    farah.industry_areas.append(documentary)  # Farah - Documentary

    hana.industry_areas.append(scripted_television)  # Hana - Scripted Television
    hana.industry_areas.append(dramatic_film)  # Hana - Dramatic Film

    iman.industry_areas.append(animation)  # Iman - Animation
    iman.industry_areas.append(commercial)  # Iman - Commercial

    lina.industry_areas.append(unscripted_television)  # Lina - Unscripted Television
    lina.industry_areas.append(documentary)  # Lina - Documentary

    mariam.industry_areas.append(scripted_television)  # Mariam - Scripted Television
    mariam.industry_areas.append(animation)  # Mariam - Animation

    nadia.industry_areas.append(dramatic_film)  # Nadia - Dramatic Film
    nadia.industry_areas.append(unscripted_television)  # Nadia - Unscripted Television

    rima.industry_areas.append(commercial)  # Rima - Commercial
    rima.industry_areas.append(documentary)  # Rima - Documentary

    yasmin.industry_areas.append(scripted_television)  # Yasmin - Scripted Television
    yasmin.industry_areas.append(dramatic_film)  # Yasmin - Dramatic Film



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
