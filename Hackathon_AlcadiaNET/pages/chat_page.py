import reflex as rx

from Hackathon_AlcadiaNET.views.navbar import navbar
from Hackathon_AlcadiaNET.views.header import header
from Hackathon_AlcadiaNET.views.footer import footer

from Hackathon_AlcadiaNET.styles.styles import Size
from Hackathon_AlcadiaNET.styles.colors import TextColor, Color

from Hackathon_AlcadiaNET.styles.styles import MAX_WIDTH
from Hackathon_AlcadiaNET.styles.styles import STYLESHEETS, MAX_WIDTH_STYLE



def chat_page() -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='en'"),
        navbar(),
        rx.center(
            rx.box(
                rx.vstack(
                    rx.image(
                        src = "/images/octocat.png",
                        width = ["100px", "150px", "200px"],
                        height = "auto",
                    ),
                    rx.box(
                        rx.box(
                            rx.text(
                                "Hello! This section was meant to be an IRC Chatroom and Forum, but couldn't be implemented due to time constraints. Sorry!",                                color = TextColor.BLACK.value,
                                font_size = ["sm", "md", "lg"],
                            ),
                            class_name = "nes-balloon from-left",
                            align = "end"
                        ),
                        margin_left = Size.SMALL.value,
                        width = ["100%", "70%", "80%"],
                    ),
                    spacing = "6",
                    align_items = "center",
                    flex_direction = ["column", "row", "row"],
                    width = "100%",
                ),
                margin_top = Size.LARGE.value,
                width = MAX_WIDTH,
                max_width = "100%",
                padding = ["1rem", "2rem", "3rem"],
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