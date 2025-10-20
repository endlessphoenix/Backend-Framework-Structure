import reflex as rx
from app.states.chat_state import ChatState, Message
from app.components.header import header_component
from app.components.footer import footer_component


def message_bubble(message: Message) -> rx.Component:
    """A single message bubble in the chat."""
    return rx.el.div(
        rx.el.p(message["content"], class_name="px-4 py-2 rounded-2xl text-white"),
        class_name=rx.cond(
            message["role"] == "user", "flex justify-end", "flex justify-start"
        ),
        style={
            "background_color": rx.cond(
                message["role"] == "user", "#2B6CB0", "#4A5568"
            ),
            "align_self": rx.cond(message["role"] == "user", "flex-end", "flex-start"),
            "border_radius": "1rem",
            "margin_bottom": "0.5rem",
            "max_width": "70%",
        },
    )


def chat_page() -> rx.Component:
    """The main chat page for the application."""
    return rx.el.div(
        header_component(),
        rx.el.main(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.h1("AI Chat", class_name="text-3xl font-bold text-white"),
                        rx.el.div(
                            rx.el.select(
                                rx.foreach(
                                    ChatState.models,
                                    lambda model: rx.el.option(model, value=model),
                                ),
                                value=ChatState.selected_model,
                                on_change=ChatState.set_selected_model,
                                class_name="bg-gray-700 text-white px-4 py-2 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500 font-semibold",
                            ),
                            rx.el.button(
                                "Clear Chat",
                                on_click=ChatState.clear_chat,
                                class_name="bg-red-600 text-white px-4 py-2 rounded-xl hover:bg-red-700 transition-colors duration-200 font-semibold",
                            ),
                            class_name="flex items-center gap-4",
                        ),
                        class_name="flex justify-between items-center mb-4",
                    ),
                    rx.el.div(
                        rx.cond(
                            ChatState.messages.length() > 0,
                            rx.foreach(ChatState.messages, message_bubble),
                            rx.el.div(
                                rx.el.p(
                                    "No messages yet. Start the conversation!",
                                    class_name="text-gray-400",
                                ),
                                class_name="flex items-center justify-center h-full",
                            ),
                        ),
                        class_name="flex-grow p-4 overflow-y-auto bg-gray-800 rounded-lg h-96",
                        id="chat-box",
                    ),
                    rx.el.form(
                        rx.el.div(
                            rx.el.input(
                                name="input_text",
                                placeholder="Type a message...",
                                class_name="flex-grow px-4 py-2 bg-gray-700 text-white rounded-l-xl focus:outline-none focus:ring-2 focus:ring-blue-500",
                            ),
                            rx.el.button(
                                rx.cond(
                                    ChatState.is_loading,
                                    rx.spinner(class_name="text-white", size="1"),
                                    rx.icon("arrow-up", class_name="text-white"),
                                ),
                                type="submit",
                                class_name="bg-blue-600 px-4 py-2 rounded-r-xl hover:bg-blue-700 transition-colors duration-200 flex items-center justify-center",
                                disabled=ChatState.is_loading,
                            ),
                            class_name="flex mt-4",
                        ),
                        on_submit=ChatState.process_message,
                        width="100%",
                        reset_on_submit=True,
                    ),
                    class_name="flex flex-col h-full",
                ),
                class_name="container mx-auto px-4 sm:px-6 lg:px-8 py-8 h-[calc(100vh-150px)]",
            ),
            class_name="flex-grow",
        ),
        footer_component(),
        class_name="font-['Roboto'] bg-gray-900 min-h-screen flex flex-col",
    )