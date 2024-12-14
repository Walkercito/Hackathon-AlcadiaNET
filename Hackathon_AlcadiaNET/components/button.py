import reflex as rx


def button(text: str, url: str, style: str, external: bool = False) -> rx.Component:
    return rx.el.button(
        text,
        class_name = f"nes-btn {style}",
        on_click = rx.redirect(
            url,
            external = True
        )
    )