import reflex as rx
from pokedex_web.components.pokedex.pokedex_header import pokedex_header
from pokedex_web.components.pokemon.image_pokemon import image_pokemon
from pokedex_web.components.pokemon.type_pokemon import type_pokemon
from pokedex_web.components.pokemon.info_pokemon import info_pokemon
from pokedex_web.components.pokemon.stats_pokemon import stats_pokemon
from pokedex_web.states.state import Pokemon


def pokedex() -> rx.Component:
    return rx.cond(
        Pokemon.pokemon_bool,
        rx.box(
            rx.box(
                pokedex_header(Pokemon.name, Pokemon.idp),
            ),
            rx.vstack(
                rx.grid(
                    rx.box(
                        image_pokemon(Pokemon.image),
                        grid_row=rx.breakpoints(initial="1", sm="1 / 3"),
                    ),
                    rx.box(
                        info_pokemon(Pokemon.height, Pokemon.weight, Pokemon.category, Pokemon.abilities, Pokemon.abilities_hidden)
                    ),
                    rx.box(
                        type_pokemon(Pokemon.types.values()),
                        grid_row="2",
                    ),
                    flow="row",
                    spacing_x="3",
                    spacing_y=rx.breakpoints(initial="3", sm="0"),
                    grid_template_columns=rx.breakpoints(initial="1fr", sm="1fr 1fr"),
                    grid_template_rows=rx.breakpoints(initial= "1fr fit-content fit-content", sm="1.7fr 0.3fr"),
                    width=rx.breakpoints(initial="calc(100% - 4rem)", sm="fit-content"),
                ),
                stats_pokemon(),
                align="center",
                width="100%"
            ),
        )
    )