import reflex as rx

from Hackathon_AlcadiaNET.styles.styles import STYLESHEETS, BASE_STYLE
from Hackathon_AlcadiaNET.views.navbar import navbar


def index() -> rx.Component:
    return rx.box(
        navbar()
    )


app = rx.App(
    stylesheets = STYLESHEETS,
    style = BASE_STYLE
)
app.add_page(
    index,
    title = "ArcadiaNET | Index",
    description = "Welcome to ArcadiaNET: A 90's inspired social network with mini-games, self-profile, forum and IRC-like chatrooms!"
    )