from pendulum import datetime, duration

from .colors import Color

USER = "xsoltis1"

REDIS_HOST = "localhost"
REDIS_PORT = 6379

CACHE_EXPIRATION = duration(days=1)

ALL_COURSES = ["pb152", "ib111", "pb161", "pv264", "pb111", "pv248"]
ACTIVE_COURSES = ["pb152", "ib111"]

SEMESTER_WEEKS = 13
SEMESTER_START = datetime(year=2023, month=9, day=18)

BLOCK_1_COLOR = Color.RED
BLOCK_2_COLOR = Color.LIME
BLOCK_3_COLOR = Color.YELLOW
BLOCK_4_COLOR = Color.BLUE
