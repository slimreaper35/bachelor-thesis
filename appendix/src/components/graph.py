from __future__ import annotations

from typing import TYPE_CHECKING

from dash import Input, Output, callback, dcc

from src.figures import FigureHandler

from .ids import ID_GRAPH, ID_RADIO_GROUP, ID_SLIDER, ID_TABS

if TYPE_CHECKING:
    from plotly.graph_objects import Figure


graph = dcc.Graph(id=ID_GRAPH, style={"height": "90vh"})


@callback(
    Output(ID_GRAPH, "figure"),
    [
        Input(ID_TABS, "value"),
        Input(ID_SLIDER, "value"),
        Input(ID_RADIO_GROUP, "value"),
    ],
)
def update_graph(
    selected_course: str,
    selected_week: int,  # noqa: ARG001
    selected_block: str,
) -> Figure:
    """Update graph based on user inputs."""
    handler = FigureHandler(course=selected_course)
    return handler.default_figure(selected_block=selected_block)
