import reflex as rx
from reflex_type_animation import type_animation

from Hackathon_AlcadiaNET.styles.styles import MAX_WIDTH_STYLE
from Hackathon_AlcadiaNET.styles.styles import FLEX_DIRECTION


def news() -> rx.Component:
    return rx.flex(
        rx.box(
            rx.text("Breaking News!", class_name = "title"),
            type_animation(
                sequence=[
                    "Scientists predict the Internet is just a fad!",
                    1000,
                    'New "Wi-Fi" tech promises no-wires connections!',
                    1000,
                    'Experts warn about the "Y2K Bug"!',
                    1000,
                    'Are "blogs" the future of communication?',
                    1000,
                    'Remember Tamagotchis? They’re still alive!',
                    1000,
                    'Dial-up internet: Who needs speed?',
                    1000,
                ],
                repeat = 1000.0,
                deletionSpeed = 1.0,
            ),
            style = MAX_WIDTH_STYLE,
            class_name = "nes-container is-dark with-title"
        ),
        flex_direction = FLEX_DIRECTION,
        style = MAX_WIDTH_STYLE,
    )