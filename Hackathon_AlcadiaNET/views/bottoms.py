import reflex as rx

from Hackathon_AlcadiaNET.styles.styles import Size
from Hackathon_AlcadiaNET.styles.colors import TextColor, Color

from Hackathon_AlcadiaNET.components.button import button
from Hackathon_AlcadiaNET.styles.styles import FLEX_DIRECTION
from Hackathon_AlcadiaNET.styles.styles import MAX_WIDTH_STYLE


def bottoms() -> rx.Component:
    return rx.box(
        rx.flex(
            rx.grid(
                button(text = "GameRoom", url = "/minigames", style = ""),
                button(text = "ChatRoom", url = "/chatroom", style = "is-primary"),
                button(text = "GuestBook", url = "/guestbook", style = ""),
                columns = rx.breakpoints(initial = "2", md = "3"),
                spacing = rx.breakpoints(initial = "4", md = "9"),
                align_items = rx.breakpoints(initial = "center", md = "center"),
            ),
            style = MAX_WIDTH_STYLE,
            border_top = f"0.25em solid {Color.SECONDARY.value}",
            border_bottom = f"0.25em solid {Color.SECONDARY.value}",
            padding_x = Size.SMALL.value,
            padding_y = Size.SMALL.value,
            margin_bottom = Size.BOTTOM.value,
        )
    )