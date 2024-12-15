import reflex as rx

from arcadiaNET.styles.styles import Size

from arcadiaNET.views.navbar import navbar
from arcadiaNET.views.header import header
from arcadiaNET.views.footer import footer
from arcadiaNET.components.news import news
from arcadiaNET.views.bottoms import bottoms
from arcadiaNET.styles.styles import MAX_WIDTH
from arcadiaNET.styles.styles import STYLESHEETS, BASE_STYLE

from arcadiaNET.pages.chat_page import chat_page
from arcadiaNET.pages.profile_page import profile_page
from arcadiaNET.pages.guestbook_page import guestbook_page
from arcadiaNET.pages.games_page import games_page



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
        width="100%",
        min_height="100vh",
        height="100%",
        bg="url('/images/bg.png')",
        background_size="cover",
        background_repeat="no-repeat",
        background_attachment="fixed",
        background_position="center"
    )


app = rx.App(
    stylesheets = STYLESHEETS,
    style = BASE_STYLE,
    state = None,
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
app.add_page(
    guestbook_page,
    image = "favicon.png",
    title = "ArcadiaNET | Guestbook",
    route = "/guestbook"
)
app.add_page(
    games_page,
    image = "favicon.png",
    title = "ArcadiaNET | Games",
    route = "/minigames"
)
app.add_custom_404_page(
    rx.container(
        rx.vstack(
            rx.heading(
                "Oops! Page Not Found",
                size = "8",
                animation = "flicker 2s infinite",
                color = "rgb(0, 255, 0)",
                style = {
                    "text-shadow": "0 0 5px #00ff00, 0 0 10px #00ff00, 0 0 15px #00ff00",
                    "@keyframes flicker": {
                        "0%": {"opacity": "1"},
                        "25%": {"opacity": "0.4"},
                        "30%": {"opacity": "1"},
                        "35%": {"opacity": "0.4"},
                        "40%": {"opacity": "1"},
                        "45%": {"opacity": "0.2"},
                        "50%": {"opacity": "1"},
                        "75%": {"opacity": "0.5"},
                        "100%": {"opacity": "1"}
                    }
                }
            ),
            rx.text(
                "It looks like the page you're looking for doesn't exist.",
                size = "5",
            ),
            spacing = "5",
            justify = "center",
            min_height = "85vh",
        ),
        rx.logo(),
    )
)