import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="/favicon.ico", widht="100px", height="auto"),
        rx.link(f"2020-{datetime.date.today().year} Noodle A.M", href="https://www.youtube.com/@NoodleAM/videos", is_external = True, _hover={"color": "red"}),
        rx.text("Building software with ♥ from Mexico to the world.", _hover={"color": "blue"}),
        align_items="center",
        justify_content="center"
    )