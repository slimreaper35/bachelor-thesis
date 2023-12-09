from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


@dataclass
class RGB:
    """RGB color representation."""

    r: int
    g: int
    b: int

    def __str__(self) -> str:
        """Return RGB color in CSS format."""
        return f"rgb({self.r}, {self.g}, {self.b})"

    def scale(self, factor: float) -> RGB:
        """Scale RGB color by `factor`."""
        return RGB(
            int(self.r * factor),
            int(self.g * factor),
            int(self.b * factor),
        )


class Color(Enum):
    """Some basic colors."""

    RED = RGB(255, 0, 0)
    LIME = RGB(0, 255, 0)
    BLUE = RGB(0, 0, 255)
    YELLOW = RGB(255, 255, 0)
    CYAN = RGB(0, 255, 255)
    MAGENTA = RGB(255, 0, 255)


def generate_n_color_shades(base: RGB, *, n: int, factor: float) -> list[RGB]:
    """Generate `n` shades of `base` RGB color by scaling it by `factor`."""
    return [base.scale(1 - (i * factor)) for i in range(n)]
