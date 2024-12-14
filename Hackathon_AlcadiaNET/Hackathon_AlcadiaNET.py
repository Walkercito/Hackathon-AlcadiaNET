import reflex as rx

from Hackathon_AlcadiaNET.styles.styles import Size

from Hackathon_AlcadiaNET.views.navbar import navbar
from Hackathon_AlcadiaNET.views.header import header
from Hackathon_AlcadiaNET.views.footer import footer
from Hackathon_AlcadiaNET.components.news import news
from Hackathon_AlcadiaNET.views.bottoms import bottoms
from Hackathon_AlcadiaNET.styles.styles import MAX_WIDTH
from Hackathon_AlcadiaNET.styles.styles import STYLESHEETS, BASE_STYLE

from Hackathon_AlcadiaNET.pages.chat_page import chat_page
from Hackathon_AlcadiaNET.pages.profile_page import profile_page



def index() -> rx.Component:
    return rx.box(
        rx.script("document.documentElement.lang='en'"),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                rx.spacer(),
                news(),
                rx.spacer(),
                rx.center(bottoms()),
                rx.spacer(),
                align = "center",
                width = "100%",
                spacing = "3"
            ),
            align = "center",
            width = "100%",
            spacing = "3"
        ),
        footer(),
        width = "100%",
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
app.add_page(
    profile_page,
    image = "favicon.png",
    title = "ArcadiaNET | Profile",
    route = "/profile"
)
app.add_page(
    chat_page,
    image = "favicon.png",
    title = "ArcadiaNET | Chat",
    route = "/chatroom"
)