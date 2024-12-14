from enum import Enum

from .fonts import Font
from .colors import Color, TextColor

MAX_WIDTH = "1000px"
FLEX_DIRECTION = ["column", "column", "column", "row", "row"]
class Size(Enum):
    SMALL = "0.5em"
    MEDIUM = "1em"
    DEFAULT = "1.5em"
    BIG = "2em"
    LARGE = "4em"


STYLESHEETS = {
    "https://unpkg.com/nes.css@latest/css/nes.min.css",
    "https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap",
}


BASE_STYLE = {
    "font_family": Font.DEFAULT.value,
    "color": TextColor.PRIMARY.value,
    "background": Color.PRIMARY.value
}