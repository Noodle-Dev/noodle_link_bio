"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import noodle_link_bio.components.navbar as nv

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
   return nv.navbar(    
    )


app = rx.App()
app.add_page(index)
