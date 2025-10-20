import reflex as rx


def footer_component() -> rx.Component:
    """The footer component for the application."""
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "© 2024 AI Framework. All rights reserved.",
                    class_name="text-sm text-gray-400",
                ),
                rx.el.a(
                    "endlessphoenix.com",
                    href="https://endlessphoenix.com",
                    target="_blank",
                    class_name="text-sm text-gray-400 hover:text-blue-400 transition-colors duration-200",
                ),
                class_name="flex flex-col sm:flex-row items-center justify-between gap-4",
            ),
            class_name="container mx-auto px-4 sm:px-6 lg:px-8",
        ),
        class_name="w-full bg-gray-900 border-t border-gray-700 py-6",
    )