import reflex as rx
from pokedex_web.components.navbar.navbar import navbar
from pokedex_web.components.pokedex.pokedex_display import pokedex


@rx.page(route="/", title="MyPokédex")
def index() -> rx.Component:
    return rx.box(
        navbar(),
        pokedex()


    )


app = rx.App(theme=rx.theme(appearance="light", has_background=True))
app.add_page(index)