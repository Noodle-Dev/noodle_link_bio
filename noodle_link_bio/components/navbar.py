import reflex as rx

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "Welcome to Noodle Link Bio tilin",
            font_size="2em",
            font_weight="bold",
            color="red",
            ),
            postion="sticky",
            bg="white",
            width="100%",
            height="100px",
            padding_x="10px",
            padding_y="8px",
            justify="center",
            align="center",
            border_radius="10px",
            shadow="md",
            
    )