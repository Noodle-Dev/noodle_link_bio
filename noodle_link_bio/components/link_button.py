import reflex as rx

def link_button(text : str, url : str) -> rx.Component:
    """Creates a button that links to a URL."""
    return rx.link(
        rx.button(text),
        href=url,
        is_external=True,
        align_items="center",  # Centra los elementos horizontalmente
        justify_content="center",  # Centra los elementos verticalmente (opcional)
        width="100%",  # Asegura que el VStack ocupe todo el ancho disponible
    )