from __future__ import annotations

from dataclasses import dataclass
from itertools import repeat
from pathlib import Path
from typing import TYPE_CHECKING

import plotly.express as px
import plotly.graph_objects as go
from polars import DataFrame, sum_horizontal

from .colors import RGB, generate_n_color_shades
from .db import DatabaseConfig, NewDatabaseCursor
from .decorators import cache_in_redis
from .settings import BLOCK_1_COLOR, BLOCK_2_COLOR, BLOCK_3_COLOR, BLOCK_4_COLOR, USER

if TYPE_CHECKING:
    from plotly.graph_objects import Figure


SRC_DIR = Path(__file__).parent
SQL_SCRIPTS = SRC_DIR.joinpath("sql")


def _generate_shades_palette() -> list[RGB]:
    palette = []

    palette.extend(generate_n_color_shades(BLOCK_1_COLOR.value, n=4, factor=0.20))
    palette.extend(generate_n_color_shades(BLOCK_2_COLOR.value, n=5, factor=0.15))
    palette.extend(generate_n_color_shades(BLOCK_3_COLOR.value, n=5, factor=0.15))
    palette.extend(generate_n_color_shades(BLOCK_4_COLOR.value, n=2, factor=0.40))

    return palette


@dataclass
class FigureHandler:
    """Handler for figure generation."""

    course: str

    def default_figure(self, selected_block: str) -> Figure:
        """Return default bar plot for all courses."""
        data_frame = init_df(self.course).sort(by=[selected_block, "total"])

        displayed_columns = list(
            filter(
                lambda x: not x.endswith("total"),
                data_frame.columns,
            ),
        )
        palette = _generate_shades_palette()
        color_map = dict(zip(displayed_columns, map(str, palette), strict=True))

        bar = px.bar(
            data_frame,
            x=None,
            y=displayed_columns,
            color_discrete_map=color_map,
            labels={"index": "students", "value": "points"},
        )

        summary = go.Scatter(
            x=None,
            y=data_frame["total"],
            mode="lines",
            name="summary",
            line={"color": "black", "width": 2},
        )

        minimum_points = 240
        minimum = go.Scatter(
            x=None,
            y=list(repeat(minimum_points, len(data_frame))),
            mode="lines",
            name="minimum",
            line={"color": "black", "width": 2},
            hoverinfo="skip",
        )

        bar.add_trace(summary)
        bar.add_trace(minimum)

        bar.update_layout(legend_title_text="")
        return bar


@cache_in_redis
def init_df(course: str) -> DataFrame:
    """Initialize data frame for given course."""
    data_frame = _load_df(course)
    displayed_columns = data_frame.columns.copy()

    b1_cols = filter(lambda x: x.startswith("b1"), displayed_columns)
    b2_cols = filter(lambda x: x.startswith("b2"), displayed_columns)
    b3_cols = filter(lambda x: x.startswith("b3"), displayed_columns)
    b4_cols = filter(lambda x: x.startswith("b4"), displayed_columns)

    data_frame = data_frame.with_columns(
        [
            sum_horizontal(b1_cols).alias("b1_total"),
            sum_horizontal(b2_cols).alias("b2_total"),
            sum_horizontal(b3_cols).alias("b3_total"),
            sum_horizontal(b4_cols).alias("b4_total"),
            sum_horizontal(data_frame.columns).alias("total"),
        ],
    )

    for col in displayed_columns:
        data_frame.replace(col, data_frame[col].apply(lambda x: max(x, 0)))

    return data_frame


def _load_df(course: str) -> DataFrame:
    config = DatabaseConfig(
        dbname=course,
        user=USER,
        host="frag-db.fi.muni.cz",
        port=5432,
    )

    with NewDatabaseCursor(config=config) as cursor:
        query = SQL_SCRIPTS.joinpath("main.sql").read_text()
        cursor.execute(query)
        data = cursor.fetchall()
        if cursor.description is not None:
            columns = [col.name for col in cursor.description]
        else:
            msg = "No data returned from database."
            raise RuntimeError(msg)

    return DataFrame(data=data, schema=columns)
