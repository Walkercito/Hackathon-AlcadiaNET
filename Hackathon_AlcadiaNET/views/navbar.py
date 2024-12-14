import reflex as rx

from Hackathon_AlcadiaNET.styles.styles import Size
from Hackathon_AlcadiaNET.styles.colors import TextColor, Color


def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.text(
                "Walkecito"
            ),
            width = "100%"
        ),
        bg = Color.PRIMARY.value,
        position = "sticky",
        border_bottom = f"0.25em solid {Color.SECONDARY.value}",
        padding_x = Size.MEDIUM.value,
        padding_y = Size.MEDIUM.value,
        z_index = "999",
        width = "100%",
        top = "0"
    )