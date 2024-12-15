import reflex as rx


def text_link(text: str, href: str) -> rx.Component:
    return rx.link(
        text,
        href = href,
    )