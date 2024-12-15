from enum import Enum
import reflex as rx

from .fonts import Font
from .colors import Color, TextColor

MAX_WIDTH = "1000px"
FLEX_DIRECTION = ["column", "column", "column", "row", "row"]
class Size(Enum):
    ZERO = "0px !important"
    TINY = "0.4em"
    SMALL = "0.5em"
    AVARAGE = "0.8em"
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
    #"background": Color.PRIMARY.value,
    rx.link: {
        "font_family": Font.DEFAULT.value,
        "_active": {
            "outline": "none",
            "box_shadow": "none",
        },
        "color": Color.PRIMARY.value,
        "text_decoration": "none",
        "_hover": {},
        "user_select": "none",
        "-webkit-user-select": "none",
        "-moz-user-select": "none",
        "-ms-user-select": "none",
    },
}


MAX_WIDTH_STYLE = dict(
    max_width = MAX_WIDTH,
    width = "100%",
    align_items = "start",
    padding_x = Size.BIG.value,
    align = "center"
)