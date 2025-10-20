import reflex as rx
from typing import TypedDict, NotRequired


class SubMenuItem(TypedDict):
    title: str
    path: str


class MenuItem(TypedDict):
    title: str
    path: NotRequired[str]
    children: NotRequired[list[SubMenuItem]]


class HeaderState(rx.State):
    """State for the header component."""

    menu_items: list[MenuItem] = [
        {"title": "Home", "path": "/"},
        {
            "title": "AI Apps",
            "children": [{"title": "AI Takeoffs", "path": "/ai-takeoffs"}],
        },
        {
            "title": "AI Support",
            "children": [
                {"title": "AI Help Desk", "path": "#"},
                {"title": "AI Website Chat", "path": "#"},
            ],
        },
        {
            "title": "AI Marketing",
            "children": [
                {"title": "AI SEO", "path": "#"},
                {"title": "AI SEM", "path": "#"},
                {"title": "AI Branding", "path": "#"},
            ],
        },
        {"title": "AI Finance", "path": "#"},
        {"title": "AI Policies", "path": "#"},
        {"title": "AI Training", "path": "#"},
        {"title": "AI Chat", "path": "/chat"},
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