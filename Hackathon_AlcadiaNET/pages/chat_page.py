import reflex as rx

from Hackathon_AlcadiaNET.views.navbar import navbar
from Hackathon_AlcadiaNET.views.header import header
from Hackathon_AlcadiaNET.views.footer import footer
from Hackathon_AlcadiaNET.state.state import ChatState

from Hackathon_AlcadiaNET.styles.styles import Size

from Hackathon_AlcadiaNET.styles.styles import MAX_WIDTH
from Hackathon_AlcadiaNET.styles.styles import STYLESHEETS, MAX_WIDTH_STYLE


def qa(question: str, answer: str) -> rx.Component:
    return rx.vstack(
        rx.text(question),
        rx.text(answer),
        width = "100%",
    )


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            ChatState.messages,
            lambda messages: qa(messages[0], messages[1]),
        )
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=ChatState.current_message,
            placeholder="Type a message",
            on_change = ChatState.set_current_message,
        ),
        rx.button(
            "Send",
            on_click = ChatState.send_message,
        ),
    )


def chat_page() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                rx.box(
                    rx.text(
                        "Chatroom",
                        class_name = "title",
                    ),
                    chat(),
                    class_name = "nes-container is-dark with-title is-centered",
                    width = "100%",
                    height = "100%",
                ),
                action_bar(),
                align="center",
            ),

        ),
        footer(),
        width = "100%",
        height = "100%",
    )