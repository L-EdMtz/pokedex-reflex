import reflex as rx
from pokedex_web.states.state import Pokemon

def bar_stat(value: rx.Var[int], max_value: int = 255) -> rx.Component:
    value = value.to(int)
    percent = f"{(value * 100) / max_value:.1f}%"

    color = (
        rx.cond(
            value < 46,
            "#fa5858",
            rx.cond(
                value < 60,
                "#faac58",
                rx.cond(
                    value < 80,
                    "#f7d358",
                    rx.cond(
                        value < 101,
                        "#f4fa58",
                        rx.cond(
                            value < 120,
                            "#78e152",
                            "#58faac"
                        )
                    )
                ),
            ),
        ),
    )

    return rx.box(
        rx.box(
            width=percent,
            height="100%",
            background_color=color,
            border_radius="999px"
        ),
        width="10rem",
        height="0.8rem",
        background_color="#ddd",
        border_radius="999px",
    )

def stat(stats: rx.Var[tuple[str, int]]) -> rx.Component:

    return rx.table.row(
        rx.table.row_header_cell(stats[0]),
        rx.table.cell(stats[1], justify="center"),
        rx.table.cell(bar_stat(stats[1]), justify="center"),
        align="center",
    ),



def stats_pokemon() -> rx.Component:
    return rx.box(
        rx.table.root(
            rx.table.header(
                    rx.table.column_header_cell(
                        "Base Stats",
                        col_span=3,
                        justify="center",
                    ),
                background_color="#E8EBF0",
            ),
            rx.table.body(
                rx.foreach(Pokemon.stats.items(), stat),
                background_color="#F6F7F9",
            ),
            width="100%",
            size="1",
            variant="ghost",
            border_radius="1rem",
            overflow="hidden",
            border="1px solid #D8DEE5",
        ),
        width=rx.breakpoints(initial="calc(100% - 4rem)", sm="600px"),
        margin_bottom="1rem"
    )