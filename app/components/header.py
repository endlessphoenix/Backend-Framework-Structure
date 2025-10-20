import reflex as rx
from app.states.header_state import HeaderState, MenuItem


def dropdown_item(text: str) -> rx.Component:
    """A single item in a dropdown menu."""
    return rx.el.a(
        text,
        href="#",
        class_name="block px-4 py-2 text-sm text-gray-300 hover:bg-gray-700 hover:text-white transition-colors duration-150",
        role="menuitem",
    )


def menu_item(item: MenuItem) -> rx.Component:
    """A single menu item, which could be a link or a dropdown."""
    return rx.el.div(
        rx.el.a(
            rx.el.p(
                item["title"],
                rx.cond(
                    item.contains("children"),
                    rx.icon("chevron-down", class_name="ml-1 h-4 w-4"),
                    rx.fragment(),
                ),
                class_name=rx.cond(
                    HeaderState.active_page == item["title"],
                    "text-blue-400 font-semibold flex items-center",
                    "text-gray-400 font-medium flex items-center",
                ),
            ),
            href="#",
            on_click=lambda: HeaderState.set_active_page(item["title"]),
            class_name="px-3 py-2 rounded-lg hover:bg-gray-800 transition-colors duration-200 ease-in-out",
        ),
        rx.cond(
            item.contains("children"),
            rx.el.div(
                rx.el.div(
                    rx.foreach(item["children"], dropdown_item), class_name="py-1"
                ),
                class_name="absolute mt-2 w-48 rounded-md shadow-lg bg-gray-800 ring-1 ring-black ring-opacity-5 focus:outline-none origin-top-right transition-all duration-200 ease-out "
                + rx.cond(
                    HeaderState.open_dropdown == item["title"],
                    "opacity-100 scale-100",
                    "opacity-0 scale-95 pointer-events-none",
                ),
                role="menu",
                aria_orientation="vertical",
            ),
            rx.fragment(),
        ),
        class_name="relative",
        on_mouse_enter=lambda: HeaderState.set_open_dropdown(item["title"]),
        on_mouse_leave=lambda: HeaderState.set_open_dropdown(""),
    )


def header_component() -> rx.Component:
    """The main header component for the application."""
    return rx.el.header(
        rx.el.div(
            rx.el.div(
                rx.icon("codesandbox", class_name="h-8 w-8 text-blue-500"),
                rx.el.h1(
                    "AI Framework",
                    class_name="text-xl font-bold text-white tracking-tight",
                ),
                class_name="flex items-center gap-3",
            ),
            rx.el.nav(
                rx.el.div(
                    rx.foreach(HeaderState.menu_items, menu_item),
                    class_name="flex items-center gap-2",
                ),
                class_name="hidden lg:flex",
            ),
            rx.el.div(
                rx.el.button(
                    rx.icon("menu", class_name="h-6 w-6 text-gray-300"),
                    class_name="p-2 rounded-md hover:bg-gray-800 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-blue-500",
                ),
                class_name="flex items-center lg:hidden",
            ),
            class_name="container mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between",
        ),
        class_name="w-full bg-gray-900/80 backdrop-blur-md sticky top-0 z-50 border-b border-gray-700 py-3",
    )