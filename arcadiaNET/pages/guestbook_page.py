import reflex as rx

from arcadiaNET.views.profile_navbar import navbar
from arcadiaNET.views.header import header
from arcadiaNET.views.footer import footer

from arcadiaNET.styles.styles import Size
from arcadiaNET.styles.colors import TextColor, Color
from arcadiaNET.components.button import button

from arcadiaNET.components.news import news
from arcadiaNET.views.bottoms import bottoms
from arcadiaNET.styles.styles import MAX_WIDTH
from arcadiaNET.styles.styles import STYLESHEETS, MAX_WIDTH_STYLE



def guestbook_page() -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='en'"),
        navbar(),
        rx.center(
            rx.box(
                rx.flex(
                    rx.vstack(
                        rx.center(
                            rx.box(
                                rx.text("Guestbook", class_name = "title", font_size = {
                                    "base": "xl",
                                    "md": "2xl",
                                    "lg": "3xl"
                                }),
                                rx.vstack(
                                    rx.box(
                                        rx.hstack(
                                            rx.box(size = {
                                                "base": "md",
                                                "md": "lg",
                                                "lg": "xl"},
                                                class_name = "nes-mario",
                                            ),
                                            rx.vstack(
                                                rx.text("@GameMaster42", font_size = {
                                                    "base": "md",
                                                    "md": "lg",
                                                    "lg": "xl"
                                                },
                                                color = TextColor.ACCENT.value,
                                                ),
                                                rx.text("Amazing retro website! Love the NES style!", font_size = {
                                                    "base": "md",
                                                    "md": "lg",
                                                    "lg": "xl"
                                                }),
                                                spacing = "2",
                                                align = "start",
                                            ),
                                            width = "100%",
                                            spacing = "6",
                                            align = "center",
                                            padding = "4",
                                        ),
                                        class_name = "nes-container is-dark",
                                        width = "100%",
                                        margin_bottom = "4",
                                    ),
                                    rx.box(
                                        rx.hstack(
                                            rx.box(size = {
                                                "base": "md",
                                                "md": "lg",
                                                "lg": "xl"},
                                                class_name = "nes-kirby",
                                            ),
                                            rx.vstack(
                                                rx.text("@RetroFan99", font_size = {
                                                    "base": "md",
                                                    "md": "lg",
                                                    "lg": "xl"
                                                },
                                                color = TextColor.ACCENT.value,
                                                ),
                                                rx.text("This takes me back to the good old days! Keep up the great work!", font_size = {
                                                    "base": "md",
                                                    "md": "lg",
                                                    "lg": "xl"
                                                }),
                                                spacing = "2",
                                                align = "start",
                                            ),
                                            width = "100%",
                                            spacing = "6",
                                            align = "center",
                                            padding = "4",
                                        ),
                                        class_name = "nes-container is-dark",
                                        width = "100%",
                                        margin_bottom = "4",
                                    ),
                                    rx.box(
                                        rx.hstack(
                                            rx.box(size = {
                                                "base": "md",
                                                "md": "lg",
                                                "lg": "xl"},
                                                class_name = "nes-pokeball",
                                            ),
                                            rx.vstack(
                                                rx.text("@PixelArtist", font_size = {
                                                    "base": "md",
                                                    "md": "lg",
                                                    "lg": "xl"
                                                },
                                                color = TextColor.ACCENT.value,
                                                ),
                                                rx.text("The pixel art and design choices are perfect! Nostalgia overload!", font_size = {
                                                    "base": "md",
                                                    "md": "lg",
                                                    "lg": "xl"
                                                }),
                                                spacing = "2",
                                                align = "start",
                                            ),
                                            width = "100%",
                                            spacing = "6",
                                            align = "center",
                                            padding = "4",
                                        ),
                                        class_name = "nes-container is-dark",
                                        width = "100%",
                                        margin_bottom = "4",
                                    ),
                                    width = "100%",
                                    spacing = "4",
                                    padding = "4"
                                ),
                                rx.center(button(
                                    text = "Leave a message",
                                    url = "/message",
                                    style = "is-primary"
                                ), margin_top = Size.DEFAULT.value),
                                class_name="nes-container is-dark with-title",
                                width={
                                    "base": "100%",
                                    "md": "80%",
                                    "lg": "60%"
                                },
                                height = "100%",
                                padding = "6",
                                spacing = Size.SMALL.value,
                            ),
                        ),
                        align="center",
                        width="100%",
                        spacing="6"
                    ),
                    align = "center",
                    width = "100%",
                    spacing = "6",
                ),
                width=MAX_WIDTH,
                max_width="100%",
                margin_top = Size.BIG.value,
                margin_bottom = Size.BOTTOM.value,
                padding={
                    "base": "4",
                    "md": "6",
                    "lg": "8"
                }
            )
        ),
        footer(),
        width="100%",
        height="100%",
        bg="url('/images/bg.png')",
        background_size="cover",
        background_repeat="no-repeat",
        background_attachment="fixed",
        background_position="center",
        overflow_x="hidden"
    )