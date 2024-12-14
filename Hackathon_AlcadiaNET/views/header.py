import reflex as rx

from Hackathon_AlcadiaNET.styles.styles import Size
from Hackathon_AlcadiaNET.styles.styles import MAX_WIDTH
from Hackathon_AlcadiaNET.styles.colors import TextColor, Color


def header() -> rx.Component:
    return rx.vstack(
        rx.heading("Welcome to, ArcadiaNET", size = "7", padding_bottom = Size.DEFAULT.value),
        rx.flex(
            rx.image(
                src = "logo.png", 
                alt = "ArcadiaNET logo", 
                width = "16em", 
                height = "16em",
                margin_right = Size.MEDIUM.value
                ),
            rx.box(
                rx.text("Your gateway to the digital frontier of the 90's!"),
            )
        ),
        max_width = MAX_WIDTH,
        align = "center"
    )