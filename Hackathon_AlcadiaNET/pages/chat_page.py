import reflex as rx

from Hackathon_AlcadiaNET.views.navbar import navbar
from Hackathon_AlcadiaNET.views.header import header
from Hackathon_AlcadiaNET.views.footer import footer

from Hackathon_AlcadiaNET.styles.styles import Size

from Hackathon_AlcadiaNET.styles.styles import MAX_WIDTH
from Hackathon_AlcadiaNET.styles.styles import STYLESHEETS, MAX_WIDTH_STYLE



def chat_page() -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='en'"),
        navbar(),
        rx.center(
            rx.box(
                # Add content here in the body
                width=MAX_WIDTH,
                max_width="100%"
            )
        ),
        footer(),
        width = "100%",
        bg = "url('/images/bg.png')",
        background_size = "cover",
        background_repeat = "no-repeat",
        background_attachment = "fixed",
        background_position = "center"
    )