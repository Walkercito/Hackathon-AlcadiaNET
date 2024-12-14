import reflex as rx

from Hackathon_AlcadiaNET.views.navbar import navbar
from Hackathon_AlcadiaNET.views.header import header
from Hackathon_AlcadiaNET.views.footer import footer
from Hackathon_AlcadiaNET.state.state import ChatState

from Hackathon_AlcadiaNET.styles.styles import Size

from Hackathon_AlcadiaNET.styles.styles import MAX_WIDTH
from Hackathon_AlcadiaNET.styles.styles import STYLESHEETS, MAX_WIDTH_STYLE



def profile_page() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(

            )
        ),
        footer(),
    )