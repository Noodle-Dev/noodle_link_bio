import reflex as rx
from noodle_link_bio.components.navbar import navbar
from noodle_link_bio.views.header.header import header
from noodle_link_bio.views.links.links import links
from noodle_link_bio.components.footer import footer
import noodle_link_bio.styles.styles as styles
from noodle_link_bio.styles.styles import Size

class State(rx.State):
   pass

def index() -> rx.Component:
   return rx.box(
      navbar(),
      rx.center(
         rx.vstack(
            header(),
            links(),
            max_width=styles.MAX_WIDTH, #Styles max width
            width="100%",
            margin_y=Size.BIG,),   # #Styles spacer.BIG
      ),
      footer()
   )  

app = rx.App(
   style=styles.BASE_STYLE,
)
app.add_page(index)
