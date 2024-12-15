import reflex as rx

from Hackathon_AlcadiaNET.views.profile_navbar import navbar
from Hackathon_AlcadiaNET.views.header import header
from Hackathon_AlcadiaNET.views.footer import footer

from Hackathon_AlcadiaNET.styles.styles import Size
from Hackathon_AlcadiaNET.styles.colors import TextColor, Color
from Hackathon_AlcadiaNET.components.button import button

from Hackathon_AlcadiaNET.components.news import news
from Hackathon_AlcadiaNET.views.bottoms import bottoms
from Hackathon_AlcadiaNET.styles.styles import MAX_WIDTH
from Hackathon_AlcadiaNET.styles.styles import STYLESHEETS, MAX_WIDTH_STYLE



def profile_page() -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='en'"),
        navbar(),
        rx.center(
            rx.box(
                rx.flex(
                    rx.vstack(
                        rx.center(
                            rx.box(
                                rx.text("My profile", class_name = "title", font_size = {
                                    "base": "xl",
                                    "md": "2xl",
                                    "lg": "3xl"
                                }),
                                rx.hstack(
                                    rx.box(size = {
                                        "base": "md",
                                        "md": "lg",
                                        "lg": "xl"},
                                        class_name = "nes-ash",
                                    ),
                                    rx.vstack(
                                        rx.text("Walkercito", font_size = {
                                            "base": "md",
                                            "md": "lg",
                                            "lg": "xl"
                                        },
                                        color = TextColor.ACCENT.value,
                                        ),
                                        rx.text("Bio: A cozy guy!", font_size = {
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
                                    margin_bottom = Size.DEFAULT.value,
                                ),
                                rx.box(
                                    rx.text("Stats", class_name="title", font_size={
                                        "base": "lg",
                                        "md": "xl",
                                        "lg": "2xl"
                                    }),
                                    rx.vstack(
                                        rx.text("Sent messages: 12", font_size = {
                                            "base": "md",
                                            "md": "lg",
                                            "lg": "xl"
                                        }),
                                        rx.text("Friends: 3", font_size = {
                                            "base": "md",
                                            "md": "lg",
                                            "lg": "xl"
                                        }),
                                        rx.text("Favorite games: Tamagotchi, Mineswaper", font_size = {
                                            "base": "md",
                                            "md": "lg",
                                            "lg": "xl"
                                        }),
                                        width = "100%",
                                        spacing = "6",
                                        align = "start",
                                        padding = "4"
                                    ),
                                    class_name = "nes-container is-dark with-title",
                                    width = "100%",
                                    height = "100%",
                                    margin_top = "6"
                                ),
                                rx.center(button(
                                    text = "Edit profile",
                                    url = "/edit",
                                    style = "is-success"
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