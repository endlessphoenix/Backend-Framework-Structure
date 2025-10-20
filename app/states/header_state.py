import reflex as rx
from typing import TypedDict, NotRequired


class MenuItem(TypedDict):
    title: str
    children: NotRequired[list[str]]


class HeaderState(rx.State):
    """State for the header component."""

    menu_items: list[MenuItem] = [
        {"title": "Home"},
        {"title": "AI Apps", "children": ["AI Takeoffs"]},
        {"title": "AI Support", "children": ["AI Help Desk", "AI Website Chat"]},
        {"title": "AI Marketing", "children": ["AI SEO", "AI SEM", "AI Branding"]},
        {"title": "AI Finance"},
        {"title": "AI Policies"},
        {"title": "AI Training"},
        {"title": "AI Chat"},
    ]
    active_page: str = "Home"
    open_dropdown: str = ""

    @rx.event
    def set_active_page(self, page: str):
        """Sets the currently active page."""
        self.active_page = page

    @rx.event
    def set_open_dropdown(self, dropdown_title: str):
        """Sets the currently open dropdown menu."""
        if self.open_dropdown == dropdown_title:
            return
        self.open_dropdown = dropdown_title