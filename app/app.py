import reflex as rx
from app.components.header import header_component
from app.components.footer import footer_component
from app.pages.chat import chat_page


def index() -> rx.Component:
    return rx.el.div(
        header_component(),
        rx.el.main(
            rx.el.div(
                rx.el.div(
                    rx.el.h1(
                        "Welcome to AI Framework",
                        class_name="text-4xl md:text-5xl font-extrabold text-white mb-4 tracking-tighter",
                    ),
                    rx.el.p(
                        "Your central hub for building next-generation AI applications.",
                        class_name="text-lg text-gray-300 mb-8 max-w-2xl mx-auto",
                    ),
                    rx.el.div(
                        rx.el.button(
                            "Get Started",
                            rx.icon("arrow-right", class_name="ml-2", size=18),
                            class_name="bg-blue-600 text-white px-6 py-3 rounded-xl hover:bg-blue-700 transition-transform duration-200 ease-in-out hover:scale-105 shadow-lg hover:shadow-blue-500/30 flex items-center font-semibold",
                        ),
                        rx.el.button(
                            "View Docs",
                            class_name="bg-gray-700 text-white px-6 py-3 rounded-xl hover:bg-gray-600 border border-gray-600 transition-colors duration-200 font-semibold shadow-sm",
                        ),
                        class_name="flex items-center justify-center gap-4",
                    ),
                    class_name="flex flex-col items-center justify-center text-center py-20 md:py-32",
                ),
                class_name="container mx-auto px-4 sm:px-6 lg:px-8",
            ),
            class_name="flex-grow",
        ),
        footer_component(),
        class_name="font-['Roboto'] bg-gray-900 min-h-screen flex flex-col",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700;900&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index)
app.add_page(chat_page, route="/chat")