import reflex as rx

def button(text: str, url: str, style: str) -> rx.Component:
    return rx.link(
        rx.el.button(
            text,
            class_name = f"nes-btn {style}",
        ),
        href = url,
        is_external = False
    )