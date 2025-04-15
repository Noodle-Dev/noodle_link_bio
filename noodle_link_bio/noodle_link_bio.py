import reflex as rx
from noodle_link_bio.components.navbar import navbar
from noodle_link_bio.views.header.header import header
from noodle_link_bio.views.links.links import links
from noodle_link_bio.components.footer import footer
import noodle_link_bio.styles as styles

class State(rx.State):
   pass

def index() -> rx.Component:
   return rx.box(
      navbar(),
      rx.center(
         rx.vstack(
            header(),
            links(),
            max_width="600px",
            width="100%",
            margin_y="30px",),
      ),
      footer()
   )  

app = rx.App()
app.add_page(index)
