import reflex as rx

from Hackathon_AlcadiaNET.styles.styles import Size

from Hackathon_AlcadiaNET.views.navbar import navbar
from Hackathon_AlcadiaNET.views.header import header
from Hackathon_AlcadiaNET.styles.styles import MAX_WIDTH
from Hackathon_AlcadiaNET.styles.styles import STYLESHEETS, BASE_STYLE


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                header(),
                header(),
            ),
            align = "center",
            width = "100%",
            spacing = "7"
        )
    )


app = rx.App(
    stylesheets = STYLESHEETS,
    style = BASE_STYLE,
    
)
app.add_page(
    index,
    image = "favicon.png",
    title = "ArcadiaNET | Index",
    description = "Welcome to ArcadiaNET: A 90's inspired social network with mini-games, self-profile, forum and IRC-like chatrooms!"
    )