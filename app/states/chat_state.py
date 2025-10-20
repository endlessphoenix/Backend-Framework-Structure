import reflex as rx
import os
import logging
from openai import OpenAI
from typing import TypedDict


class Message(TypedDict):
    role: str
    content: str


class ChatState(rx.State):
    """State for the chat component."""

    messages: list[Message] = []
    is_loading: bool = False

    @rx.event(background=True)
    async def process_message(self, form_data: dict[str, str]):
        """Processes the user's message and gets a response from the AI."""
        input_text = form_data.get("input_text", "").strip()
        if not input_text:
            return
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        async with self:
            self.is_loading = True
            self.messages.append({"role": "user", "content": input_text})
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo", messages=self.messages, max_tokens=150
            )
            ai_message = response.choices[0].message.content
            async with self:
                self.messages.append({"role": "assistant", "content": ai_message})
        except Exception as e:
            logging.exception(f"Error processing message: {e}")
            async with self:
                self.messages.append({"role": "assistant", "content": f"Error: {e}"})
        finally:
            async with self:
                self.is_loading = False

    @rx.event
    def clear_chat(self):
        """Clears the chat history."""
        self.messages = []