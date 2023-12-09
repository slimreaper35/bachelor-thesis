import dash_mantine_components as dmc

from .graph import graph
from .radio_group import radio_group
from .slider import slider
from .tabs import tabs

base = dmc.Container(
    [
        tabs,
        dmc.Grid(
            [
                dmc.Col(radio_group, span=1),
                dmc.Col(graph, span="auto"),
            ],
            align="center",
        ),
        slider,
    ],
    fluid=True,
)
