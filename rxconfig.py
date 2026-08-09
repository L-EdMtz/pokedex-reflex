import reflex as rx

config = rx.Config(
    app_name="pokedex_web",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)