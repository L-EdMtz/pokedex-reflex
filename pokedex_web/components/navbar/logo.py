import reflex as rx


def logo() -> rx.Component:
    return rx.hstack(
        rx.image(
            src="/logo_pokemon.png",
            width="auto",
            height="3.5em",
        ),
        rx.heading(
            "Pokédex",
            size="7",
            weight="regular",
            color="#000000",

        ),
        width="fit-content",
        align="center",
        spacing="5",
    ),