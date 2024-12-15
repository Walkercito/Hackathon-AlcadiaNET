import reflex as rx

from Hackathon_AlcadiaNET.styles.styles import Size
from Hackathon_AlcadiaNET.styles.colors import TextColor, Color


def footer() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(
                "© 1995 ArcadiaNET",
                font_size = [f"{Size.SMALL.value}", f"{Size.AVARAGE.value}", f"{Size.AVARAGE.value}"],
            ),
            rx.text(
                "Best viewed with Netscape Navigator 3.0",
                font_size = [f"{Size.SMALL.value}", f"{Size.AVARAGE.value}", f"{Size.AVARAGE.value}"],
            ),
            align_items = "center",
        ),
        bg = Color.PRIMARY.value,
        align_items = "center",
        position = "sticky",
        border_top = f"0.10em solid {Color.SECONDARY.value}",
        padding_x = Size.SMALL.value,
        padding_y = Size.SMALL.value,
        padding_top = Size.SMALL.value,
        width = "100%",
        bottom = "0"
    )
