import reflex as rx


def show_info(info: str):
    return rx.text(
        info,
        color="black",
        size="3",
    )


def info_pokemon(height: str, weight: str, category: str, abilities: list, abilities_hidden: list) -> rx.Component:
    return rx.box(
        rx.grid(
            rx.box(
                rx.text.strong("Height:", color="black", size="3"),
                rx.text(f"{height}m", color="black"),
            ),
            rx.box(
                rx.text.strong("Weight:", color="black", size="3"),
                rx.text(f"{weight}kg", color="black"),
            ),
            rx.box(
                rx.text.strong("Hidden Abilities:", color="black", size="3"),
                rx.foreach(abilities_hidden, show_info),
                grid_column="span 2"
            ),
            rx.box(
                rx.text.strong("Category:", color="black", size="3"),
                rx.text(category, color="black"),

            ),
            rx.box(
                rx.text.strong("Abilities:", color="black", size="3"),
                rx.foreach(abilities, show_info),

            ),
            rows="3",
            grid_template_columns="0.8fr 1.2fr",
            background_color="#F8F4A6",
            border_radius="1rem",
            border="3px solid #f8f06a",
            flow="column",
            padding="1em 1em 0 1em",
            spacing_y="2",
            height="100%"
        ),
        height="250px",
        width=rx.breakpoints(initial="100%", sm="20rem")
    )

