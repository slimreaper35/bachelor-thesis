import dash_mantine_components as dmc
from pendulum import now

from src.settings import SEMESTER_START, SEMESTER_WEEKS

from .ids import ID_SLIDER

CURRENT_WEEK = (now() - SEMESTER_START).in_weeks() + 1

slider = dmc.Slider(
    id=ID_SLIDER,
    min=1,
    max=SEMESTER_WEEKS,
    step=1,
    value=CURRENT_WEEK,
    marks=[{"label": i, "value": i} for i in range(1, SEMESTER_WEEKS + 1)],
    disabled=True,
)
