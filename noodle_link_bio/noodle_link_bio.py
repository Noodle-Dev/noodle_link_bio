"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from noodle_link_bio.components.navbar import navbar
from noodle_link_bio.views.header.header import header
from noodle_link_bio.views.links.links import links
from noodle_link_bio.components.footer import footer

class State(rx.State):
   pass


def index() -> rx.Component:
   return rx.vstack(
      navbar(),
      header(),
      links(),
      footer(),
      #Alignments
      align_items="center",
      justify_content="center", 
      width="100%"  
   )


app = rx.App()
app.add_page(index)
