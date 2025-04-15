import reflex as rx

def link_button(text : str, url : str) -> rx.Component:
    """Creates a button that links to a URL."""
    return rx.link(
        rx.button(text),
        href=url,
        is_external=True,
       
    )