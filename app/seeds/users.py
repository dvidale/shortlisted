from app.models import db, User, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_users():
    # aa w
    Aaliyah_W = User(username='aaliyah.walker@example.com', email='aaliyah.walker@example.com', phone_number='2015550101', password='password', first_name='Aaliyah', last_name='Walker', profile_img_url= 'https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/aa-w/aa-f-001.jpg')
    Brianna_J = User(username='brianna.jones@example.com', email='brianna.jones@example.com', phone_number='2015550102', password='password', first_name='Brianna', last_name='Jones', profile_img_url= 'https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/aa-w/aa-f002.jpg')
    Ciara_T = User(username='ciara.taylor@example.com', email='ciara.taylor@example.com', phone_number='2015550103', password='password', first_name='Ciara', last_name='Taylor', profile_img_url= 'https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/aa-w/aa-f003.jpg')
    Deja_H = User(username='deja.harris@example.com', email='deja.harris@example.com', phone_number='2015550104', password='password', first_name='Deja', last_name='Harris', profile_img_url= 'https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/aa-w/lat-f001.jpg')
    Emani_B = User(username='emani.brown@example.com', email='emani.brown@example.com', phone_number='2015550105', password='password', first_name='Emani', last_name='Brown', profile_img_url= 'https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/aa-w/lat-f002.jpg')
    Faith_D = User(username='faith.davis@example.com', email='faith.davis@example.com', phone_number='2015550106', password='password', first_name='Faith', last_name='Davis', profile_img_url= 'https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/lat-w/Slice+2.jpg')
    Gabrielle_W = User(username='gabrielle.white@example.com', email='gabrielle.white@example.com', phone_number='2015550107', password='password', first_name='Gabrielle', last_name='White', profile_img_url= 'https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/lat-w/Slice+22.jpg')
    Halle_J = User(username='halle.jackson@example.com', email='halle.jackson@example.com', phone_number='2015550108', password='password', first_name='Halle', last_name='Jackson', profile_img_url= 'https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/lat-w/Slice+7.jpg')
    Imani_C = User(username='imani.clark@example.com', email='imani.clark@example.com', phone_number='2015550109', password='password', first_name='Imani', last_name='Clark', profile_img_url= 'https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/lat-w/sSlice+6.jpg')
    Jada_L = User(username='jada.lee@example.com', email='jada.lee@example.com', phone_number='2015550110', password='password', first_name='Jada', last_name='Lee', profile_img_url= 'https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/lat-w/sSlice+9.jpg')

    #aa m
    Aaron_M = User(username='aaron.mitchell@example.com', email='aaron.mitchell@example.com', phone_number='2015550111', password='password', first_name='Aaron', last_name='Mitchell', profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/aa-m/aa-m001.jpg')
    Brandon_C = User(username='brandon.carter@example.com', email='brandon.carter@example.com', phone_number='2015550112', password='password', first_name='Brandon', last_name='Carter', profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/aa-m/aa-m002.png')
    Caleb_R = User(username='caleb.richardson@example.com', email='caleb.richardson@example.com', phone_number='2015550113', password='password', first_name='Caleb', last_name='Richardson', profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/aa-m/aa-m003.png')
    Darius_S = User(username='darius.scott@example.com', email='darius.scott@example.com', phone_number='2015550114', password='password', first_name='Darius', last_name='Scott', profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/aa-m/aa-m004.png')
    Elijah_T = User(username='elijah.thomas@example.com', email='elijah.thomas@example.com', phone_number='2015550115', password='password', first_name='Elijah', last_name='Thomas', profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/aa-m/aa-m005.jpg')
    Franklin_B = User(username='franklin.bailey@example.com', email='franklin.bailey@example.com', phone_number='2015550116', password='password', first_name='Franklin', last_name='Bailey', profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/aa-m/aa-m006.jpg')
    Gregory_D = User(username='gregory.daniels@example.com', email='gregory.daniels@example.com', phone_number='2015550117', password='password', first_name='Gregory', last_name='Daniels', profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/aa-m/aa-m007.jpg')
    Howard_F = User(username='howard.foster@example.com', email='howard.foster@example.com', phone_number='2015550118', password='password', first_name='Howard', last_name='Foster', profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/aa-m/aa-m008.jpg')
    Isaiah_G = User(username='isaiah.griffin@example.com', email='isaiah.griffin@example.com', phone_number='2015550119', password='password', first_name='Isaiah', last_name='Griffin', profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/aa-m/aa-m009.jpg')
    Jason_H = User(username='jason.hayes@example.com', email='jason.hayes@example.com', phone_number='2015550120', password='password', first_name='Jason', last_name='Hayes', profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/aa-m/aa-m010.jpg')

    #a m
    Arjun_P = User(
    username='arjun.patel@example.com',
    email='arjun.patel@example.com',
    phone_number='2015550121',
    password='password',
    first_name='Arjun',
    last_name='Patel',
    profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/a-m/Slice+1.jpg'
    )

    Bilal_K = User(
        username='bilal.khan@example.com',
        email='bilal.khan@example.com',
        phone_number='2015550122',
        password='password',
        first_name='Bilal',
        last_name='Khan',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/a-m/Slice+2.jpg'
    )

    Chetan_S = User(
        username='chetan.sharma@example.com',
        email='chetan.sharma@example.com',
        phone_number='2015550123',
        password='password',
        first_name='Chetan',
        last_name='Sharma',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/a-m/Slice+3.jpg'
    )

    Dev_R = User(
        username='dev.raj@example.com',
        email='dev.raj@example.com',
        phone_number='2015550124',
        password='password',
        first_name='Dev',
        last_name='Raj',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/a-m/Slice+4.jpg'
    )

    Eshan_M = User(
        username='eshan.mehta@example.com',
        email='eshan.mehta@example.com',
        phone_number='2015550125',
        password='password',
        first_name='Eshan',
        last_name='Mehta',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/a-m/Slice+5.jpg'
    )

    Faisal_N = User(
        username='faisal.naidu@example.com',
        email='faisal.naidu@example.com',
        phone_number='2015550126',
        password='password',
        first_name='Faisal',
        last_name='Naidu',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/a-m/Slice+6.jpg'
    )

    Gautam_A = User(
        username='gautam.anand@example.com',
        email='gautam.anand@example.com',
        phone_number='2015550127',
        password='password',
        first_name='Gautam',
        last_name='Anand',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/a-m/Slice+7.jpg'
    )

    Harish_J = User(
        username='harish.joshi@example.com',
        email='harish.joshi@example.com',
        phone_number='2015550128',
        password='password',
        first_name='Harish',
        last_name='Joshi',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/a-m/Slice+8.jpg'
    )

    Imran_Q = User(
        username='imran.qureshi@example.com',
        email='imran.qureshi@example.com',
        phone_number='2015550129',
        password='password',
        first_name='Imran',
        last_name='Qureshi',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/a-m/Slice+9.jpg'
    )

    Jai_V = User(
        username='jai.verma@example.com',
        email='jai.verma@example.com',
        phone_number='2015550130',
        password='password',
        first_name='Jai',
        last_name='Verma',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/a-m/wSlice+1.jpg'
    )

    # a w
    Kavya_M = User(
    username='kavya.malhotra@example.com',
    email='kavya.malhotra@example.com',
    phone_number='2015550131',
    password='password',
    first_name='Kavya',
    last_name='Malhotra',
    profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/a-w/rSlice+1.jpg'
    )

    Lata_N = User(
        username='lata.nair@example.com',
        email='lata.nair@example.com',
        phone_number='2015550132',
        password='password',
        first_name='Lata',
        last_name='Nair',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/a-w/rSlice+2.jpg'
    )

    Meera_P = User(
        username='meera.patel@example.com',
        email='meera.patel@example.com',
        phone_number='2015550133',
        password='password',
        first_name='Meera',
        last_name='Patel',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/a-w/rSlice+3.jpg'
    )

    Naina_R = User(
        username='naina.raj@example.com',
        email='naina.raj@example.com',
        phone_number='2015550134',
        password='password',
        first_name='Naina',
        last_name='Raj',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/a-w/rSlice+4.jpg'
    )

    Oorja_S = User(
        username='oorja.singh@example.com',
        email='oorja.singh@example.com',
        phone_number='2015550135',
        password='password',
        first_name='Oorja',
        last_name='Singh',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/a-w/rSlice+5.jpg'
    )

    Pooja_K = User(
        username='pooja.kumar@example.com',
        email='pooja.kumar@example.com',
        phone_number='2015550136',
        password='password',
        first_name='Pooja',
        last_name='Kumar',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/a-w/rSlice+6.jpg'
    )

    Qadira_T = User(
        username='qadira.tiwari@example.com',
        email='qadira.tiwari@example.com',
        phone_number='2015550137',
        password='password',
        first_name='Qadira',
        last_name='Tiwari',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/a-w/rSlice+7.jpg'
    )

    Rani_A = User(
        username='rani.ahuja@example.com',
        email='rani.ahuja@example.com',
        phone_number='2015550138',
        password='password',
        first_name='Rani',
        last_name='Ahuja',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/a-w/rSlice+8.jpg'
    )

    Sanya_M = User(
        username='sanya.mehta@example.com',
        email='sanya.mehta@example.com',
        phone_number='2015550139',
        password='password',
        first_name='Sanya',
        last_name='Mehta',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/a-w/rSlice+9.jpg'
    )

    Tanvi_V = User(
        username='tanvi.varma@example.com',
        email='tanvi.varma@example.com',
        phone_number='2015550140',
        password='password',
        first_name='Tanvi',
        last_name='Varma',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/a-w/Slice+1.jpg'
    )

    # h w
    Elena_S = User(
    username='elena.santos@example.com',
    email='elena.santos@example.com',
    phone_number='2015550151',
    password='password',
    first_name='Elena',
    last_name='Santos',
    profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/lat-w/Slice+2.jpg'
    )

    Frida_T = User(
        username='frida.torres@example.com',
        email='frida.torres@example.com',
        phone_number='2015550152',
        password='password',
        first_name='Frida',
        last_name='Torres',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/lat-w/Slice+22.jpg'
    )

    Gabriela_U = User(
        username='gabriela.uribe@example.com',
        email='gabriela.uribe@example.com',
        phone_number='2015550153',
        password='password',
        first_name='Gabriela',
        last_name='Uribe',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/lat-w/Slice+7.jpg'
    )

    Helena_V = User(
        username='helena.velasquez@example.com',
        email='helena.velasquez@example.com',
        phone_number='2015550154',
        password='password',
        first_name='Helena',
        last_name='Velasquez',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/lat-w/sSlice+6.jpg'
    )

    Isabella_W = User(username='isabella.williams@example.com', email='isabella.williams@example.com', phone_number='2015550155', password='password', first_name='Isabella', last_name='Williams', profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/lat-w/sSlice+9.jpg')
    Juana_X = User(username='juana.ximenez@example.com', email='juana.ximenez@example.com', phone_number='2015550156', password='password', first_name='Juana', last_name='Ximenez', profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/lat-w/tSlice+2.jpg')
    Karla_Y = User(username='karla.ybarra@example.com', email='karla.ybarra@example.com', phone_number='2015550157', password='password', first_name='Karla', last_name='Ybarra', profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/lat-w/tSlice+6.jpg')
    Lucia_Z = User(username='lucia.zaragoza@example.com', email='lucia.zaragoza@example.com', phone_number='2015550158', password='password', first_name='Lucia', last_name='Zaragoza', profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/lat-w/Slice+2.jpg')
    Mariana_A = User(username='mariana.alonso@example.com', email='mariana.alonso@example.com', phone_number='2015550159', password='password', first_name='Mariana', last_name='Alonso', profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/lat-w/Slice+22.jpg')
    Natalia_B = User(username='natalia.barrera@example.com', email='natalia.barrera@example.com', phone_number='2015550160', password='password', first_name='Natalia', last_name='Barrera', profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/lat-w/Slice+7.jpg')

    # w w
    Olivia_C = User(
    username='olivia.clark@example.com',
    email='olivia.clark@example.com',
    phone_number='2015550161',
    password='password',
    first_name='Olivia',
    last_name='Clark',
    profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/w-w/fSlice+3.jpg'
    )

    Penelope_D = User(
        username='penelope.dunn@example.com',
        email='penelope.dunn@example.com',
        phone_number='2015550162',
        password='password',
        first_name='Penelope',
        last_name='Dunn',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/w-w/Slice+1.jpg'
    )

    Quinn_E = User(
        username='quinn.ellis@example.com',
        email='quinn.ellis@example.com',
        phone_number='2015550163',
        password='password',
        first_name='Quinn',
        last_name='Ellis',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/w-w/Slice+2.jpg'
    )

    Rachel_F = User(
        username='rachel.ford@example.com',
        email='rachel.ford@example.com',
        phone_number='2015550164',
        password='password',
        first_name='Rachel',
        last_name='Ford',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/a-w/Slice+1.jpg'
    )

    Sophia_G = User(
        username='sophia.gray@example.com',
        email='sophia.gray@example.com',
        phone_number='2015550165',
        password='password',
        first_name='Sophia',
        last_name='Gray',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/a-w/Slice+2.jpg'
    )

    Tiffany_H = User(
        username='tiffany.hunt@example.com',
        email='tiffany.hunt@example.com',
        phone_number='2015550166',
        password='password',
        first_name='Tiffany',
        last_name='Hunt',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/a-w/Slice+3.jpg'
    )

    Ursula_I = User(
        username='ursula.ingram@example.com',
        email='ursula.ingram@example.com',
        phone_number='2015550167',
        password='password',
        first_name='Ursula',
        last_name='Ingram',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/a-w/Slice+4.jpg'
    )

    Victoria_J = User(
        username='victoria.jones@example.com',
        email='victoria.jones@example.com',
        phone_number='2015550168',
        password='password',
        first_name='Victoria',
        last_name='Jones',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/a-w/Slice+5.jpg'
    )

    Wendy_K = User(
        username='wendy.knight@example.com',
        email='wendy.knight@example.com',
        phone_number='2015550169',
        password='password',
        first_name='Wendy',
        last_name='Knight',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/a-w/Slice+6.jpg'
    )

    Xena_L = User(
        username='xena.lambert@example.com',
        email='xena.lambert@example.com',
        phone_number='2015550170',
        password='password',
        first_name='Xena',
        last_name='Lambert',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/a-w/Slice+7.jpg'
    )

    # w m

    Aaron_M = User(
    username='aaron.miller@example.com',
    email='aaron.miller@example.com',
    phone_number='2015550171',
    password='password',
    first_name='Aaron',
    last_name='Miller',
    profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/w-m/fSlice+1.jpg'
    )

    Brian_N = User(
        username='brian.nelson@example.com',
        email='brian.nelson@example.com',
        phone_number='2015550172',
        password='password',
        first_name='Brian',
        last_name='Nelson',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/w-m/fSlice+2.jpg'
    )

    Cameron_O = User(
        username='cameron.owens@example.com',
        email='cameron.owens@example.com',
        phone_number='2015550173',
        password='password',
        first_name='Cameron',
        last_name='Owens',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/w-m/fSlice+4.jpg'
    )

    Dylan_P = User(
        username='dylan.parker@example.com',
        email='dylan.parker@example.com',
        phone_number='2015550174',
        password='password',
        first_name='Dylan',
        last_name='Parker',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/w-m/Slice+3.jpg'
    )

    Ethan_Q = User(
        username='ethan.quinn@example.com',
        email='ethan.quinn@example.com',
        phone_number='2015550175',
        password='password',
        first_name='Ethan',
        last_name='Quinn',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/w-m/Slice+4.jpg'
    )

    Felix_R = User(
        username='felix.ross@example.com',
        email='felix.ross@example.com',
        phone_number='2015550176',
        password='password',
        first_name='Felix',
        last_name='Ross',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/a-m/xSlice+1.jpg'
    )

    Gavin_S = User(
        username='gavin.stone@example.com',
        email='gavin.stone@example.com',
        phone_number='2015550177',
        password='password',
        first_name='Gavin',
        last_name='Stone',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/a-m/xSlice+2.jpg'
    )

    Henry_T = User(
        username='henry.taylor@example.com',
        email='henry.taylor@example.com',
        phone_number='2015550178',
        password='password',
        first_name='Henry',
        last_name='Taylor',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/a-m/xSlice+3.jpg'
    )

    Ian_U = User(
        username='ian.underwood@example.com',
        email='ian.underwood@example.com',
        phone_number='2015550179',
        password='password',
        first_name='Ian',
        last_name='Underwood',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/a-m/xSlice+4.jpg'
    )

    Jack_V = User(
        username='jack.vance@example.com',
        email='jack.vance@example.com',
        phone_number='2015550180',
        password='password',
        first_name='Jack',
        last_name='Vance',
        profile_img_url='https://aa-portfolio-08-2024.s3.us-east-2.amazonaws.com/shortlisted-app/seed-profile-images/a-m/xSlice+6.jpg'
    )

    user_list = [
    Aaliyah_W,
    Brianna_J,
    Ciara_T,
    Deja_H,
    Emani_B,
    Faith_D,
    Gabrielle_W,
    Halle_J,
    Imani_C,
    Jada_L,
    Aaron_M,
    Brandon_C,
    Caleb_R,
    Darius_S,
    Elijah_T,
    Franklin_B,
    Gregory_D,
    Howard_F,
    Isaiah_G,
    Jason_H,
    Arjun_P,
    Bilal_K,
    Chetan_S,
    Dev_R,
    Eshan_M,
    Faisal_N,
    Gautam_A,
    Harish_J,
    Imran_Q,
    Jai_V,
    Kavya_M,
    Lata_N,
    Meera_P,
    Naina_R,
    Oorja_S,
    Pooja_K,
    Qadira_T,
    Rani_A,
    Sanya_M,
    Tanvi_V,
    Elena_S,
    Frida_T,
    Gabriela_U,
    Helena_V,
    Isabella_W,
    Juana_X,
    Karla_Y,
    Lucia_Z,
    Mariana_A,
    Natalia_B,
    Olivia_C,
    Penelope_D,
    Quinn_E,
    Rachel_F,
    Sophia_G,
    Tiffany_H,
    Ursula_I,
    Victoria_J,
    Wendy_K,
    Xena_L,
    Aaron_M,
    Brian_N,
    Cameron_O,
    Dylan_P,
    Ethan_Q,
    Felix_R,
    Gavin_S,
    Henry_T,
    Ian_U,
    Jack_V
]



    db.session.add_all(user_list)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))
        
    db.session.commit()
