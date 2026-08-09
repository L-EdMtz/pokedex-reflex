import reflex as rx
from pokedex_web.components.navbar.logo import logo
from pokedex_web.components.navbar.searchbar import searchbar


def navbar() -> rx.Component:
    return rx.vstack(
        rx.flex(
            logo(),
            searchbar(),

            direction=rx.breakpoints(initial="column", sm="row"),
            justify=rx.breakpoints(initial="center" ,sm="between"),
            align="center",
            spacing="3",
            width="100%",
            padding="1.8em",
            background_color="#ff0100"
        ),
        rx.box(
            background_color="black",
            width="100%",
            height="1.5em"
        ),
        spacing="0"
    )

