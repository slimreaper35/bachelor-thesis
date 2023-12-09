import dash_mantine_components as dmc
from dash import Dash

from .components.containers import base

app = Dash(title="Frag")

app.layout = dmc.MantineProvider(
    base,
    theme={"primaryColor": "dark"},
    withNormalizeCSS=True,
    withGlobalStyles=True,
    inherit=True,
)

server = app.server
