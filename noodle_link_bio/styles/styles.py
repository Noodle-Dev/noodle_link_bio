from enum import Enum
import reflex as rx
# CONSTANTS
MAX_WIDTH = "600px"

#Sizes
class Size(Enum):
    SMALL = "0.5em"
    DEFAULT = "1em"
    BIG = "2em"


BASE_STYLE = {
    rx.button : {
        "width" : "100%",
        "height" : "100%",
        "display" : "block",
        "padding" : Size.SMALL.value,
        "border_radius" : Size.DEFAULT.value,
        
    },
    rx.link : {
        # PlaceHOlders 3>09
         "text_decoration" : "none",
        "width" : "100%",
        "color" : "black",
    },
}