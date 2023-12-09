import dash_mantine_components as dmc

from .ids import ID_RADIO_GROUP

radio_group = dmc.RadioGroup(
    id=ID_RADIO_GROUP,
    children=[
        dmc.Radio(label="b1_total", value="b1_total"),
        dmc.Radio(label="b2_total", value="b2_total"),
        dmc.Radio(label="b3_total", value="b3_total"),
        dmc.Radio(label="b4_total", value="b4_total"),
        dmc.Radio(label="total", value="total"),
    ],
    value="total",
    orientation="vertical",
)
