import reflex as rx

from arcadiaNET.views.navbar import navbar
from arcadiaNET.views.header import header
from arcadiaNET.views.footer import footer

from arcadiaNET.styles.styles import Size

from arcadiaNET.styles.styles import MAX_WIDTH
from arcadiaNET.styles.styles import STYLESHEETS, MAX_WIDTH_STYLE



def guestbook_page() -> rx.Component:
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
        width="100%",
        height="100vh",
        bg="url('/images/bg.png')",
        background_size="cover",
        background_repeat="no-repeat",
        background_attachment="fixed",
        background_position="center"
    )