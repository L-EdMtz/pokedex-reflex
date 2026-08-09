import reflex as rx
from pokedex_web.states.state import Pokemon


def searchbar() -> rx.Component :
    return rx.form(
                rx.hstack(
                    rx.input(
                        value=Pokemon.pokemon,
                        placeholder="Name or number",
                        on_change=Pokemon.set_pokemon,
                        radius="large",
                        color_scheme="red",
                        size="3",

                    ),
                    rx.button(
                        rx.icon("search"),
                        type="submit",
                        color_scheme="gray",
                        high_contrast=True,
                        radius="large",
                        size="3",
                    ),
                    spacing="1",
                ),
                width="fit-content",
                on_submit=Pokemon.get_pokemon,
            ),