import reflex as rx

from arcadiaNET.styles.styles import Size
from arcadiaNET.styles.colors import TextColor, Color

from arcadiaNET.components.button import button


def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.link(
                "ArcadiaNET",
                href = "/",
                font_size = [f"{Size.MEDIUM.value}", f"{Size.DEFAULT.value}", f"{Size.DEFAULT.value}"], color = "#fdfb76", style = {"textShadow": "1px 1px 2px rgba(234, 89, 64, 0.5)"}
            ),
            rx.spacer(),            
            button(
                "Profile",
                "/profile",
                "is-warning",
            ),
            align="center",
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