import dash_mantine_components as dmc

from src.settings import ACTIVE_COURSES, ALL_COURSES

from .ids import ID_TABS

tabs = dmc.Tabs(
    id=ID_TABS,
    value=ACTIVE_COURSES[0],
    children=[
        dmc.TabsList(
            [
                dmc.Tab(
                    course.upper(),
                    value=course,
                    disabled=bool(course not in ACTIVE_COURSES),
                )
                for course in ALL_COURSES
            ],
            grow=True,
        ),
    ],
)
