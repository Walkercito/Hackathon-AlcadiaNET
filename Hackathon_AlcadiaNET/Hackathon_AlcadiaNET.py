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
from Hackathon_AlcadiaNET.pages.guestbook_page import guestbook_page
from Hackathon_AlcadiaNET.pages.games_page import games_page



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
        height="100vh",
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