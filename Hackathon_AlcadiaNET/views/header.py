import reflex as rx

from Hackathon_AlcadiaNET.styles.styles import Size
from Hackathon_AlcadiaNET.styles.styles import MAX_WIDTH
from Hackathon_AlcadiaNET.styles.styles import FLEX_DIRECTION
from Hackathon_AlcadiaNET.styles.styles import MAX_WIDTH_STYLE
from Hackathon_AlcadiaNET.styles.colors import TextColor, Color


def header() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Welcome to ArcadiaNET",
            size = "7",
            padding_bottom = Size.DEFAULT.value,
            color = "#EA5940",
            style = {
                "textShadow": "1px 1px 2px rgba(234, 89, 64, 0.5)"
            }
        ),
        rx.flex(
            rx.image(
                src = "logo.png",
                alt="ArcadiaNET logo",
                width="16em",
                height="16em",
                margin_right=Size.MEDIUM.value
            ),
            rx.box(
                rx.text(
                    "Your gateway to the digital frontier of the 90's!",
                    color=TextColor.TERCIARY.value
                ),
            ),
            align_items="start",
            flex_direction=FLEX_DIRECTION
        ),
        style=MAX_WIDTH_STYLE,
        padding_top=Size.BIG.value,
    )