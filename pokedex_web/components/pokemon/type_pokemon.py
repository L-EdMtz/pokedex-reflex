import reflex as rx

def show_type(type_pkm: str) -> rx.Component:
    return rx.image(
        type_pkm,
        width="auto",
        height=rx.breakpoints(initial="1.2rem", sm="1.3rem"),
    )

def type_pokemon(types_pkm: list) -> rx.Component:
    return rx.vstack(
        rx.text(
            "Type:",
            size=rx.breakpoints(initial="4", sm="5")

        ),
        rx.hstack(
            rx.foreach(types_pkm, show_type),
            spacing="2",


        ),
        spacing="2",
        width=rx.breakpoints(initial="100%", sm="20rem")
    )