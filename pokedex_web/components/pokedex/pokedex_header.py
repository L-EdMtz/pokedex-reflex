import reflex as rx
from pokedex_web.states.state import Pokemon


def pokedex_header(name: str, id_pkm: str) -> rx.Component:
    return rx.hstack(
        rx.button(
            rx.icon(
                "arrow_left",
                stroke_width=3,
                size=22
            ),
            on_click=Pokemon.res_pokemon,
            color_scheme="blue",
            size="3"
        ),
        rx.box(
            rx.flex(
                rx.text(
                    name,
                    
                    size=rx.breakpoints(initial="6", sm="7")
                ),
                rx.text(
                    f"N.° {id_pkm}",
                    color_scheme="gray",
                    size=rx.breakpoints(initial="6", sm="7")
                ),
                direction=rx.breakpoints(initial="column", sm="row"),
                justify="center",
                align="center",
                spacing=rx.breakpoints(initial="1", sm="3")

            ),
            width=rx.breakpoints(initial="60%", sm="40%")

        ),
        rx.button(
            rx.icon(
                "arrow_right",
                stroke_width=3,
                size=22
            ),
            on_click=Pokemon.sum_pokemon,
            color_scheme="blue",
            size="3"
        ),
        justify="center",
        align="center",
        margin_y="1em"
    )




