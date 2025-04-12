import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(fallback="Noodle AM"),
        rx.text("Que pedo"),
        rx.text("Noodle A.M"),
        rx.text("A simple app to manage your links"),

        align_items="center",  # Centra los elementos horizontalmente
        justify_content="center",  # Centra los elementos verticalmente (opcional)
        width="100%",  # Asegura que el VStack ocupe todo el ancho disponible
    )