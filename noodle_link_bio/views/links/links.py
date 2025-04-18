import reflex as rx
from noodle_link_bio.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
         link_button("Link 1", "https://x.com/noodle_stud1"),
         link_button("Link 2", "https://x.com/noodle_stud1"),
         width="100%",
    )