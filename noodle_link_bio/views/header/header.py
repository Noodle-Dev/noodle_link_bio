import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.image(src="/heroimage.png", width="100px", height="auto"),
        #rx.avatar(fallback="ALEX"),
        rx.text("Game developer since 2020"),
        rx.text("Noodle A.M"),

        align_items="center",  # Centra los elementos horizontalmente
        justify_content="center",  # Centra los elementos verticalmente (opcional)
        width="100%",  # Asegura que el VStack ocupe todo el ancho disponible
    )