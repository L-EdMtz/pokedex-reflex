import reflex as rx

def image_pokemon(img: str) -> rx.Component:
    return rx.box(
        rx.image(
            src=img,
            width="100%",
            height="100%",
            background_color="#f2f2f2",
            border_radius="1rem",
            border="3px solid #d8d8d8"
        ),
        height="auto",
        width=rx.breakpoints(initial="100%", sm="20rem")


    )


#