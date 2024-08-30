from app.models import db, Booking, environment, SCHEMA
from sqlalchemy.sql import text
from datetime import datetime



# Adds a demo user, you can add other users here if you want
def seed_bookings():
    booking_user1_1 = Booking(
    user_id=1,
    shortlist_id=None,
    start_date=datetime(2024, 8, 1),
    end_date=datetime(2024, 8, 22),
    )

    booking_user1_2 = Booking(
        user_id=1,
        shortlist_id=None,
        start_date=datetime(2024, 8, 31),
        end_date=datetime(2024, 10, 26),
    )

    booking_user2_1 = Booking(
        user_id=2,
        shortlist_id=None,
        start_date=datetime(2024, 8, 22),
        end_date=datetime(2024, 9, 12),
    )

    booking_user2_2 = Booking(
        user_id=2,
        shortlist_id=None,
        start_date=datetime(2024, 9, 21),
        end_date=datetime(2024, 11, 16),
    )

    booking_user3_1 = Booking(
        user_id=3,
        shortlist_id=None,
        start_date=datetime(2024, 9, 13),
        end_date=datetime(2024, 10, 4),
    )

    booking_user3_2 = Booking(
        user_id=3,
        shortlist_id=None,
        start_date=datetime(2024, 10, 13),
        end_date=datetime(2024, 12, 8),
    )

    booking_user4_1 = Booking(
        user_id=4,
        shortlist_id=None,
        start_date=datetime(2024, 10, 4),
        end_date=datetime(2024, 10, 25),
    )

    booking_user4_2 = Booking(
        user_id=4,
        shortlist_id=None,
        start_date=datetime(2024, 11, 3),
        end_date=datetime(2024, 12, 29),
    )

    booking_user5_1 = Booking(
        user_id=5,
        shortlist_id=None,
        start_date=datetime(2024, 10, 25),
        end_date=datetime(2024, 11, 15),
    )

    booking_user5_2 = Booking(
        user_id=5,
        shortlist_id=None,
        start_date=datetime(2024, 11, 24),
        end_date=datetime(2025, 1, 19),
    )

    booking_user6_1 = Booking(
    user_id=6,
    shortlist_id=None,
    start_date=datetime(2024, 11, 15),
    end_date=datetime(2024, 12, 6),
    )

    booking_user6_2 = Booking(
        user_id=6,
        shortlist_id=None,
        start_date=datetime(2024, 12, 16),
        end_date=datetime(2025, 2, 10),
    )

    booking_user7_1 = Booking(
        user_id=7,
        shortlist_id=None,
        start_date=datetime(2024, 12, 6),
        end_date=datetime(2024, 12, 27),
    )

    booking_user7_2 = Booking(
        user_id=7,
        shortlist_id=None,
        start_date=datetime(2025, 1, 6),
        end_date=datetime(2025, 3, 2),
    )

    booking_user8_1 = Booking(
        user_id=8,
        shortlist_id=None,
        start_date=datetime(2024, 12, 27),
        end_date=datetime(2025, 1, 17),
    )

    booking_user8_2 = Booking(
        user_id=8,
        shortlist_id=None,
        start_date=datetime(2025, 1, 27),
        end_date=datetime(2025, 3, 23),
    )

    booking_user9_1 = Booking(
        user_id=9,
        shortlist_id=None,
        start_date=datetime(2025, 1, 17),
        end_date=datetime(2025, 2, 7),
    )

    booking_user9_2 = Booking(
        user_id=9,
        shortlist_id=None,
        start_date=datetime(2025, 2, 17),
        end_date=datetime(2025, 4, 13),
    )

    booking_user10_1 = Booking(
        user_id=10,
        shortlist_id=None,
        start_date=datetime(2024, 9, 1),
        end_date=datetime(2024, 9, 22),
    )

    booking_user10_2 = Booking(
        user_id=10,
        shortlist_id=None,
        start_date=datetime(2024, 10, 2),
        end_date=datetime(2024, 12, 27),
    )

    booking_user11_1 = Booking(
    user_id=11,
    shortlist_id=None,
    start_date=datetime(2024, 8, 8),
    end_date=datetime(2024, 8, 29),
    )

    booking_user11_2 = Booking(
        user_id=11,
        shortlist_id=None,
        start_date=datetime(2024, 9, 8),
        end_date=datetime(2024, 11, 3),
    )

    booking_user12_1 = Booking(
        user_id=12,
        shortlist_id=None,
        start_date=datetime(2024, 8, 29),
        end_date=datetime(2024, 9, 19),
    )

    booking_user12_2 = Booking(
        user_id=12,
        shortlist_id=None,
        start_date=datetime(2024, 10, 19),
        end_date=datetime(2024, 12, 14),
    )

    booking_user13_1 = Booking(
        user_id=13,
        shortlist_id=None,
        start_date=datetime(2024, 9, 19),
        end_date=datetime(2024, 10, 10),
    )

    booking_user13_2 = Booking(
        user_id=13,
        shortlist_id=None,
        start_date=datetime(2024, 11, 10),
        end_date=datetime(2025, 1, 4),
    )

    booking_user14_1 = Booking(
        user_id=14,
        shortlist_id=None,
        start_date=datetime(2024, 10, 10),
        end_date=datetime(2024, 10, 31),
    )

    booking_user14_2 = Booking(
        user_id=14,
        shortlist_id=None,
        start_date=datetime(2024, 11, 30),
        end_date=datetime(2025, 1, 25),
    )

    booking_user15_1 = Booking(
        user_id=15,
        shortlist_id=None,
        start_date=datetime(2024, 10, 31),
        end_date=datetime(2024, 11, 21),
    )

    booking_user15_2 = Booking(
        user_id=15,
        shortlist_id=None,
        start_date=datetime(2025, 1, 20),
        end_date=datetime(2025, 3, 17),
    )

    booking_user16_1 = Booking(
        user_id=16,
        shortlist_id=None,
        start_date=datetime(2024, 11, 21),
        end_date=datetime(2024, 12, 12),
    )

    booking_user16_2 = Booking(
        user_id=16,
        shortlist_id=None,
        start_date=datetime(2025, 1, 11),
        end_date=datetime(2025, 3, 8),
    )

    booking_user17_1 = Booking(
        user_id=17,
        shortlist_id=None,
        start_date=datetime(2024, 12, 12),
        end_date=datetime(2025, 1, 2),
    )

    booking_user17_2 = Booking(
        user_id=17,
        shortlist_id=None,
        start_date=datetime(2025, 2, 1),
        end_date=datetime(2025, 3, 29),
    )

    booking_user18_1 = Booking(
        user_id=18,
        shortlist_id=None,
        start_date=datetime(2025, 1, 2),
        end_date=datetime(2025, 1, 23),
    )

    booking_user18_2 = Booking(
        user_id=18,
        shortlist_id=None,
        start_date=datetime(2025, 2, 22),
        end_date=datetime(2025, 4, 19),
    )

    booking_user19_1 = Booking(
        user_id=19,
        shortlist_id=None,
        start_date=datetime(2025, 1, 23),
        end_date=datetime(2025, 2, 13),
    )

    booking_user19_2 = Booking(
        user_id=19,
        shortlist_id=None,
        start_date=datetime(2025, 3, 14),
        end_date=datetime(2025, 5, 9),
    )

    booking_user20_1 = Booking(
        user_id=20,
        shortlist_id=None,
        start_date=datetime(2025, 2, 13),
        end_date=datetime(2025, 3, 6),
    )

    booking_user20_2 = Booking(
        user_id=20,
        shortlist_id=None,
        start_date=datetime(2025, 4, 5),
        end_date=datetime(2025, 5, 31),
    )

    booking_user21_1 = Booking(
    user_id=21,
    shortlist_id=None,
    start_date=datetime(2025, 3, 6),
    end_date=datetime(2025, 3, 27),
    )

    booking_user21_2 = Booking(
        user_id=21,
        shortlist_id=None,
        start_date=datetime(2025, 4, 26),
        end_date=datetime(2025, 6, 21),
    )

    booking_user22_1 = Booking(
        user_id=22,
        shortlist_id=None,
        start_date=datetime(2025, 3, 27),
        end_date=datetime(2025, 4, 17),
    )

    booking_user22_2 = Booking(
        user_id=22,
        shortlist_id=None,
        start_date=datetime(2025, 5, 17),
        end_date=datetime(2025, 7, 12),
    )

    booking_user23_1 = Booking(
        user_id=23,
        shortlist_id=None,
        start_date=datetime(2025, 4, 17),
        end_date=datetime(2025, 5, 8),
    )

    booking_user23_2 = Booking(
        user_id=23,
        shortlist_id=None,
        start_date=datetime(2025, 6, 7),
        end_date=datetime(2025, 8, 2),
    )

    booking_user24_1 = Booking(
        user_id=24,
        shortlist_id=None,
        start_date=datetime(2025, 5, 8),
        end_date=datetime(2025, 5, 29),
    )

    booking_user24_2 = Booking(
        user_id=24,
        shortlist_id=None,
        start_date=datetime(2025, 6, 28),
        end_date=datetime(2025, 8, 23),
    )

    booking_user25_1 = Booking(
        user_id=25,
        shortlist_id=None,
        start_date=datetime(2025, 5, 29),
        end_date=datetime(2025, 6, 19),
    )

    booking_user25_2 = Booking(
        user_id=25,
        shortlist_id=None,
        start_date=datetime(2025, 7, 19),
        end_date=datetime(2025, 9, 13),
    )

    booking_user26_1 = Booking(
        user_id=26,
        shortlist_id=None,
        start_date=datetime(2025, 6, 19),
        end_date=datetime(2025, 7, 10),
    )

    booking_user26_2 = Booking(
        user_id=26,
        shortlist_id=None,
        start_date=datetime(2025, 8, 9),
        end_date=datetime(2025, 10, 4),
    )

    booking_user27_1 = Booking(
        user_id=27,
        shortlist_id=None,
        start_date=datetime(2025, 7, 10),
        end_date=datetime(2025, 7, 31),
    )

    booking_user27_2 = Booking(
        user_id=27,
        shortlist_id=None,
        start_date=datetime(2025, 8, 30),
        end_date=datetime(2025, 10, 25),
    )

    booking_user28_1 = Booking(
        user_id=28,
        shortlist_id=None,
        start_date=datetime(2025, 7, 31),
        end_date=datetime(2025, 8, 21),
    )

    booking_user28_2 = Booking(
        user_id=28,
        shortlist_id=None,
        start_date=datetime(2025, 9, 20),
        end_date=datetime(2025, 11, 15),
    )

    booking_user29_1 = Booking(
        user_id=29,
        shortlist_id=None,
        start_date=datetime(2025, 8, 21),
        end_date=datetime(2025, 9, 11),
    )

    booking_user29_2 = Booking(
        user_id=29,
        shortlist_id=None,
        start_date=datetime(2025, 10, 11),
        end_date=datetime(2025, 12, 6),
    )

    booking_user30_1 = Booking(
        user_id=30,
        shortlist_id=None,
        start_date=datetime(2025, 9, 11),
        end_date=datetime(2025, 10, 2),
    )

    booking_user30_2 = Booking(
        user_id=30,
        shortlist_id=None,
        start_date=datetime(2025, 11, 1),
        end_date=datetime(2025, 12, 27),
    )

    booking_user31_1 = Booking(
    user_id=31,
    shortlist_id=None,
    start_date=datetime(2025, 10, 2),
    end_date=datetime(2025, 10, 23),
    )

    booking_user31_2 = Booking(
        user_id=31,
        shortlist_id=None,
        start_date=datetime(2025, 11, 22),
        end_date=datetime(2025, 1, 17),
    )

    booking_user32_1 = Booking(
        user_id=32,
        shortlist_id=None,
        start_date=datetime(2025, 10, 23),
        end_date=datetime(2025, 11, 13),
    )

    booking_user32_2 = Booking(
        user_id=32,
        shortlist_id=None,
        start_date=datetime(2025, 12, 13),
        end_date=datetime(2025, 2, 7),
    )

    booking_user33_1 = Booking(
        user_id=33,
        shortlist_id=None,
        start_date=datetime(2025, 11, 13),
        end_date=datetime(2025, 12, 4),
    )

    booking_user33_2 = Booking(
        user_id=33,
        shortlist_id=None,
        start_date=datetime(2025, 1, 3),
        end_date=datetime(2025, 2, 28),
    )

    booking_user34_1 = Booking(
        user_id=34,
        shortlist_id=None,
        start_date=datetime(2025, 12, 4),
        end_date=datetime(2025, 12, 25),
    )

    booking_user34_2 = Booking(
        user_id=34,
        shortlist_id=None,
        start_date=datetime(2025, 2, 24),
        end_date=datetime(2025, 4, 20),
    )

    booking_user35_1 = Booking(
        user_id=35,
        shortlist_id=None,
        start_date=datetime(2025, 12, 25),
        end_date=datetime(2025, 1, 15),
    )

    booking_user35_2 = Booking(
        user_id=35,
        shortlist_id=None,
        start_date=datetime(2025, 2, 14),
        end_date=datetime(2025, 4, 11),
    )

    booking_user36_1 = Booking(
        user_id=36,
        shortlist_id=None,
        start_date=datetime(2025, 1, 15),
        end_date=datetime(2025, 2, 5),
    )

    booking_user36_2 = Booking(
        user_id=36,
        shortlist_id=None,
        start_date=datetime(2025, 3, 5),
        end_date=datetime(2025, 4, 30),
    )

    booking_user37_1 = Booking(
        user_id=37,
        shortlist_id=None,
        start_date=datetime(2025, 2, 5),
        end_date=datetime(2025, 2, 26),
    )

    booking_user37_2 = Booking(
        user_id=37,
        shortlist_id=None,
        start_date=datetime(2025, 3, 28),
        end_date=datetime(2025, 5, 23),
    )

    booking_user38_1 = Booking(
        user_id=38,
        shortlist_id=None,
        start_date=datetime(2025, 2, 26),
        end_date=datetime(2025, 3, 19),
    )

    booking_user38_2 = Booking(
        user_id=38,
        shortlist_id=None,
        start_date=datetime(2025, 4, 18),
        end_date=datetime(2025, 6, 13),
    )

    booking_user39_1 = Booking(
        user_id=39,
        shortlist_id=None,
        start_date=datetime(2025, 3, 19),
        end_date=datetime(2025, 4, 9),
    )

    booking_user39_2 = Booking(
        user_id=39,
        shortlist_id=None,
        start_date=datetime(2025, 5, 9),
        end_date=datetime(2025, 7, 4),
    )

    booking_user40_1 = Booking(
        user_id=40,
        shortlist_id=None,
        start_date=datetime(2025, 4, 9),
        end_date=datetime(2025, 4, 30),
    )

    booking_user40_2 = Booking(
        user_id=40,
        shortlist_id=None,
        start_date=datetime(2025, 5, 30),
        end_date=datetime(2025, 7, 25),
    )

    booking_user41_1 = Booking(
    user_id=41,
    shortlist_id=None,
    start_date=datetime(2025, 4, 30),
    end_date=datetime(2025, 5, 21),
    )

    booking_user41_2 = Booking(
        user_id=41,
        shortlist_id=None,
        start_date=datetime(2025, 6, 20),
        end_date=datetime(2025, 8, 15),
    )

    booking_user42_1 = Booking(
        user_id=42,
        shortlist_id=None,
        start_date=datetime(2025, 5, 21),
        end_date=datetime(2025, 6, 11),
    )

    booking_user42_2 = Booking(
        user_id=42,
        shortlist_id=None,
        start_date=datetime(2025, 7, 11),
        end_date=datetime(2025, 9, 5),
    )

    booking_user43_1 = Booking(
        user_id=43,
        shortlist_id=None,
        start_date=datetime(2025, 6, 11),
        end_date=datetime(2025, 7, 2),
    )

    booking_user43_2 = Booking(
        user_id=43,
        shortlist_id=None,
        start_date=datetime(2025, 8, 1),
        end_date=datetime(2025, 9, 26),
    )

    booking_user44_1 = Booking(
        user_id=44,
        shortlist_id=None,
        start_date=datetime(2025, 7, 2),
        end_date=datetime(2025, 7, 23),
    )

    booking_user44_2 = Booking(
        user_id=44,
        shortlist_id=None,
        start_date=datetime(2025, 8, 22),
        end_date=datetime(2025, 10, 17),
    )

    booking_user45_1 = Booking(
        user_id=45,
        shortlist_id=None,
        start_date=datetime(2025, 7, 23),
        end_date=datetime(2025, 8, 13),
    )

    booking_user45_2 = Booking(
        user_id=45,
        shortlist_id=None,
        start_date=datetime(2025, 9, 12),
        end_date=datetime(2025, 11, 7),
    )

    booking_user46_1 = Booking(
        user_id=46,
        shortlist_id=None,
        start_date=datetime(2025, 8, 13),
        end_date=datetime(2025, 9, 3),
    )

    booking_user46_2 = Booking(
        user_id=46,
        shortlist_id=None,
        start_date=datetime(2025, 10, 3),
        end_date=datetime(2025, 11, 28),
    )

    booking_user47_1 = Booking(
        user_id=47,
        shortlist_id=None,
        start_date=datetime(2025, 9, 3),
        end_date=datetime(2025, 9, 24),
    )

    booking_user47_2 = Booking(
        user_id=47,
        shortlist_id=None,
        start_date=datetime(2025, 10, 24),
        end_date=datetime(2025, 12, 19),
    )

    booking_user48_1 = Booking(
        user_id=48,
        shortlist_id=None,
        start_date=datetime(2025, 9, 24),
        end_date=datetime(2025, 10, 15),
    )

    booking_user48_2 = Booking(
        user_id=48,
        shortlist_id=None,
        start_date=datetime(2025, 11, 14),
        end_date=datetime(2025, 1, 9),
    )

    booking_user49_1 = Booking(
        user_id=49,
        shortlist_id=None,
        start_date=datetime(2025, 10, 15),
        end_date=datetime(2025, 11, 5),
    )

    booking_user49_2 = Booking(
        user_id=49,
        shortlist_id=None,
        start_date=datetime(2025, 12, 5),
        end_date=datetime(2025, 1, 30),
    )

    booking_user50_1 = Booking(
        user_id=50,
        shortlist_id=None,
        start_date=datetime(2025, 11, 5),
        end_date=datetime(2025, 11, 26),
    )

    booking_user50_2 = Booking(
        user_id=50,
        shortlist_id=None,
        start_date=datetime(2025, 12, 26),
        end_date=datetime(2025, 2, 20),
    )


    booking_user51_1 = Booking(
        user_id=51,
        shortlist_id=None,
        start_date=datetime(2025, 11, 26),
        end_date=datetime(2025, 12, 17),
    )

    booking_user51_2 = Booking(
        user_id=51,
        shortlist_id=None,
        start_date=datetime(2025, 12, 27),
        end_date=datetime(2025, 2, 21),
    )

    booking_user52_1 = Booking(
        user_id=52,
        shortlist_id=None,
        start_date=datetime(2025, 12, 17),
        end_date=datetime(2025, 1, 7),
    )

    booking_user52_2 = Booking(
        user_id=52,
        shortlist_id=None,
        start_date=datetime(2026, 1, 6),
        end_date=datetime(2026, 3, 3),
    )

    booking_user53_1 = Booking(
        user_id=53,
        shortlist_id=None,
        start_date=datetime(2025, 1, 7),
        end_date=datetime(2025, 1, 28),
    )

    booking_user53_2 = Booking(
        user_id=53,
        shortlist_id=None,
        start_date=datetime(2025, 2, 27),
        end_date=datetime(2025, 4, 24),
    )

    booking_user54_1 = Booking(
        user_id=54,
        shortlist_id=None,
        start_date=datetime(2025, 1, 28),
        end_date=datetime(2025, 2, 18),
    )

    booking_user54_2 = Booking(
        user_id=54,
        shortlist_id=None,
        start_date=datetime(2025, 3, 20),
        end_date=datetime(2025, 5, 15),
    )

    booking_user55_1 = Booking(
        user_id=55,
        shortlist_id=None,
        start_date=datetime(2025, 2, 18),
        end_date=datetime(2025, 3, 11),
    )

    booking_user55_2 = Booking(
        user_id=55,
        shortlist_id=None,
        start_date=datetime(2025, 4, 10),
        end_date=datetime(2025, 6, 5),
    )

    booking_user56_1 = Booking(
        user_id=56,
        shortlist_id=None,
        start_date=datetime(2025, 3, 11),
        end_date=datetime(2025, 4, 1),
    )

    booking_user56_2 = Booking(
        user_id=56,
        shortlist_id=None,
        start_date=datetime(2025, 5, 1),
        end_date=datetime(2025, 6, 26),
    )

    booking_user57_1 = Booking(
        user_id=57,
        shortlist_id=None,
        start_date=datetime(2025, 4, 1),
        end_date=datetime(2025, 4, 22),
    )

    booking_user57_2 = Booking(
        user_id=57,
        shortlist_id=None,
        start_date=datetime(2025, 5, 22),
        end_date=datetime(2025, 7, 17),
    )

    booking_user58_1 = Booking(
        user_id=58,
        shortlist_id=None,
        start_date=datetime(2025, 4, 22),
        end_date=datetime(2025, 5, 13),
    )

    booking_user58_2 = Booking(
        user_id=58,
        shortlist_id=None,
        start_date=datetime(2025, 6, 12),
        end_date=datetime(2025, 8, 7),
    )

    booking_user59_1 = Booking(
        user_id=59,
        shortlist_id=None,
        start_date=datetime(2025, 5, 13),
        end_date=datetime(2025, 6, 3),
    )

    booking_user59_2 = Booking(
        user_id=59,
        shortlist_id=None,
        start_date=datetime(2025, 7, 3),
        end_date=datetime(2025, 8, 28),
    )

    booking_user60_1 = Booking(
        user_id=60,
        shortlist_id=None,
        start_date=datetime(2025, 6, 3),
        end_date=datetime(2025, 6, 24),
    )

    booking_user60_2 = Booking(
        user_id=60,
        shortlist_id=None,
        start_date=datetime(2025, 7, 24),
        end_date=datetime(2025, 9, 18),
    )

    booking_user61_1 = Booking(
    user_id=61,
    shortlist_id=None,
    start_date=datetime(2025, 6, 24),
    end_date=datetime(2025, 7, 15),
    )

    booking_user61_2 = Booking(
        user_id=61,
        shortlist_id=None,
        start_date=datetime(2025, 8, 14),
        end_date=datetime(2025, 10, 9),
    )

    booking_user62_1 = Booking(
        user_id=62,
        shortlist_id=None,
        start_date=datetime(2025, 7, 15),
        end_date=datetime(2025, 8, 5),
    )

    booking_user62_2 = Booking(
        user_id=62,
        shortlist_id=None,
        start_date=datetime(2025, 9, 4),
        end_date=datetime(2025, 10, 30),
    )

    booking_user63_1 = Booking(
        user_id=63,
        shortlist_id=None,
        start_date=datetime(2025, 8, 5),
        end_date=datetime(2025, 8, 26),
    )

    booking_user63_2 = Booking(
        user_id=63,
        shortlist_id=None,
        start_date=datetime(2025, 9, 25),
        end_date=datetime(2025, 11, 20),
    )

    booking_user64_1 = Booking(
        user_id=64,
        shortlist_id=None,
        start_date=datetime(2025, 8, 26),
        end_date=datetime(2025, 9, 16),
    )

    booking_user64_2 = Booking(
        user_id=64,
        shortlist_id=None,
        start_date=datetime(2025, 10, 16),
        end_date=datetime(2025, 12, 11),
    )

    booking_user65_1 = Booking(
        user_id=65,
        shortlist_id=None,
        start_date=datetime(2025, 9, 16),
        end_date=datetime(2025, 10, 7),
    )

    booking_user65_2 = Booking(
        user_id=65,
        shortlist_id=None,
        start_date=datetime(2025, 11, 6),
        end_date=datetime(2025, 12, 31),
    )

    booking_user66_1 = Booking(
        user_id=66,
        shortlist_id=None,
        start_date=datetime(2025, 10, 7),
        end_date=datetime(2025, 10, 28),
    )

    booking_user66_2 = Booking(
        user_id=66,
        shortlist_id=None,
        start_date=datetime(2025, 11, 27),
        end_date=datetime(2025, 1, 22),
    )

    booking_user67_1 = Booking(
        user_id=67,
        shortlist_id=None,
        start_date=datetime(2025, 10, 28),
        end_date=datetime(2025, 11, 18),
    )

    booking_user67_2 = Booking(
        user_id=67,
        shortlist_id=None,
        start_date=datetime(2025, 12, 18),
        end_date=datetime(2025, 2, 12),
    )

    booking_user68_1 = Booking(
        user_id=68,
        shortlist_id=None,
        start_date=datetime(2025, 11, 18),
        end_date=datetime(2025, 12, 9),
    )

    booking_user68_2 = Booking(
        user_id=68,
        shortlist_id=None,
        start_date=datetime(2026, 1, 8),
        end_date=datetime(2026, 3, 4),
    )

    booking_user69_1 = Booking(
        user_id=69,
        shortlist_id=None,
        start_date=datetime(2025, 12, 9),
        end_date=datetime(2025, 12, 30),
    )

    booking_user69_2 = Booking(
        user_id=69,
        shortlist_id=None,
        start_date=datetime(2026, 1, 29),
        end_date=datetime(2026, 3, 25),
    )

    booking_user70_1 = Booking(
        user_id=70,
        shortlist_id=None,
        start_date=datetime(2025, 12, 30),
        end_date=datetime(2026, 1, 20),
    )

    booking_user70_2 = Booking(
        user_id=70,
        shortlist_id=None,
        start_date=datetime(2026, 2, 19),
        end_date=datetime(2026, 4, 15),
    )


    booking_variables = [
    booking_user1_1,
    booking_user1_2,
    booking_user2_1,
    booking_user2_2,
    booking_user3_1,
    booking_user3_2,
    booking_user4_1,
    booking_user4_2,
    booking_user5_1,
    booking_user5_2,
    booking_user6_1,
    booking_user6_2,
    booking_user7_1,
    booking_user7_2,
    booking_user8_1,
    booking_user8_2,
    booking_user9_1,
    booking_user9_2,
    booking_user10_1,
    booking_user10_2,
    booking_user11_1,
    booking_user11_2,
    booking_user12_1,
    booking_user12_2,
    booking_user13_1,
    booking_user13_2,
    booking_user14_1,
    booking_user14_2,
    booking_user15_1,
    booking_user15_2,
    booking_user16_1,
    booking_user16_2,
    booking_user17_1,
    booking_user17_2,
    booking_user18_1,
    booking_user18_2,
    booking_user19_1,
    booking_user19_2,
    booking_user20_1,
    booking_user20_2,
    booking_user21_1,
    booking_user21_2,
    booking_user22_1,
    booking_user22_2,
    booking_user23_1,
    booking_user23_2,
    booking_user24_1,
    booking_user24_2,
    booking_user25_1,
    booking_user25_2,
    booking_user26_1,
    booking_user26_2,
    booking_user27_1,
    booking_user27_2,
    booking_user28_1,
    booking_user28_2,
    booking_user29_1,
    booking_user29_2,
    booking_user30_1,
    booking_user30_2,
    booking_user31_1,
    booking_user31_2,
    booking_user32_1,
    booking_user32_2,
    booking_user33_1,
    booking_user33_2,
    booking_user34_1,
    booking_user34_2,
    booking_user35_1,
    booking_user35_2,
    booking_user36_1,
    booking_user36_2,
    booking_user37_1,
    booking_user37_2,
    booking_user38_1,
    booking_user38_2,
    booking_user39_1,
    booking_user39_2,
    booking_user40_1,
    booking_user40_2,
    booking_user41_1,
    booking_user41_2,
    booking_user42_1,
    booking_user42_2,
    booking_user43_1,
    booking_user43_2,
    booking_user44_1,
    booking_user44_2,
    booking_user45_1,
    booking_user45_2,
    booking_user46_1,
    booking_user46_2,
    booking_user47_1,
    booking_user47_2,
    booking_user48_1,
    booking_user48_2,
    booking_user49_1,
    booking_user49_2,
    booking_user50_1,
    booking_user50_2,
    booking_user51_1,
    booking_user51_2,
    booking_user52_1,
    booking_user52_2,
    booking_user53_1,
    booking_user53_2,
    booking_user54_1,
    booking_user54_2,
    booking_user55_1,
    booking_user55_2,
    booking_user56_1,
    booking_user56_2,
    booking_user57_1,
    booking_user57_2,
    booking_user58_1,
    booking_user58_2,
    booking_user59_1,
    booking_user59_2,
    booking_user60_1,
    booking_user60_2,
    booking_user61_1,
    booking_user61_2,
    booking_user62_1,
    booking_user62_2,
    booking_user63_1,
    booking_user63_2,
    booking_user64_1,
    booking_user64_2,
    booking_user65_1,
    booking_user65_2,
    booking_user66_1,
    booking_user66_2,
    booking_user67_1,
    booking_user67_2,
    booking_user68_1,
    booking_user68_2,
    booking_user69_1,
    booking_user69_2,
    booking_user70_1,
    booking_user70_2,
  
]


    db.session.add_all(booking_variables)


    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_bookings():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.bookings RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM bookings"))
        
    db.session.commit()
