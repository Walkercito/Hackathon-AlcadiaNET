import reflex as rx

from arcadiaNET.views.navbar import navbar
from arcadiaNET.views.header import header
from arcadiaNET.views.footer import footer

from arcadiaNET.styles.styles import Size
from arcadiaNET.components.button import button
from arcadiaNET.styles.colors import TextColor, Color

from arcadiaNET.styles.styles import MAX_WIDTH
from arcadiaNET.styles.styles import STYLESHEETS, MAX_WIDTH_STYLE


def games_page() -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='en'"),
        navbar(),
        rx.center(
            rx.box(
                rx.flex(
                    rx.vstack(
                        rx.center(
                            rx.box(
                                rx.text("Library", class_name = "title", font_size = {
                                    "base": "xl",
                                    "md": "2xl",
                                    "lg": "3xl"
                                }),
                                rx.box(
                                    rx.text("Games", class_name="title", font_size={
                                        "base": "lg",
                                        "md": "xl",
                                        "lg": "2xl"
                                    }),
                                    rx.flex(
                                        rx.grid(
                                            button(text = "Tamagotchi", url = "/no", style = "is-primary"),
                                            button(text = "Snake", url = "/no", style = "is-primary"),
                                            button(text = "Minesweeper", url = "/no", style = "is-primary"),
                                            button(text = "Tetris", url = "/no", style = "is-primary"),
                                            button(text = "Pong", url = "/no", style = "is-primary"),
                                            button(text = "Space Invaders", url = "/no", style = "is-primary"),
                                            template_columns={
                                                "base": "repeat(1, 1fr)",
                                                "md": "repeat(2, 1fr)",
                                                "lg": "repeat(3, 1fr)"
                                            },
                                            gap="4",
                                            width="100%",
                                            padding="4"
                                        ),
                                        width="100%",
                                        justify="center",
                                        align="center"
                                    ),
                                    class_name = "nes-container is-dark with-title",
                                    width = "100%",
                                    height = "100%",
                                    margin_top = "6"
                                ),
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
                padding={
                    "base": "4",
                    "md": "6",
                    "lg": "8"
                }
            )
        ),
        footer(),
        width="100%",
        height="100vh",
        bg="url('/images/bg.png')",
        background_size="cover",
        background_repeat="no-repeat",
        background_attachment="fixed",
        background_position="center"
    )