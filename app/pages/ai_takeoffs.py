import reflex as rx
from app.states.takeoff_state import TakeoffState
from app.components.header import header_component
from app.components.footer import footer_component

UPLOAD_ID = "takeoff_upload"


def file_display(file_name: str) -> rx.Component:
    """Displays an uploaded file with a file icon."""
    return rx.el.div(
        rx.icon("file-text", class_name="w-4 h-4 mr-2 text-gray-400"),
        rx.el.span(file_name, class_name="text-sm text-gray-300"),
        class_name="flex items-center bg-gray-700 p-2 rounded-md",
    )


def upload_area() -> rx.Component:
    """The file upload drag-and-drop area."""
    return rx.upload.root(
        rx.el.div(
            rx.icon("cloud-upload", class_name="w-10 h-10 text-gray-500 mb-3"),
            rx.el.p(
                "Drop project files here", class_name="text-blue-400 font-semibold"
            ),
            rx.el.p(
                "(PDF, CSV, JSON) or click to browse",
                class_name="text-xs text-gray-500",
            ),
            class_name="text-center p-8",
        ),
        id=UPLOAD_ID,
        accept={
            "application/pdf": [".pdf"],
            "text/csv": [".csv"],
            "application/json": [".json"],
        },
        multiple=True,
        class_name="w-full h-full border-2 border-dashed border-gray-600 rounded-xl cursor-pointer hover:bg-gray-800/50 transition-colors duration-200 flex flex-col items-center justify-center",
    )


def ai_takeoffs_page() -> rx.Component:
    """The AI Takeoffs page for uploading project files."""
    return rx.el.div(
        header_component(),
        rx.el.main(
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "Project Input", class_name="text-2xl font-bold text-white mb-6"
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.div(
                                rx.cond(
                                    TakeoffState.uploaded_files.length() == 0,
                                    upload_area(),
                                    rx.el.div(
                                        rx.foreach(
                                            TakeoffState.uploaded_files, file_display
                                        ),
                                        class_name="space-y-2 p-4 h-48 overflow-y-auto bg-gray-900/50 rounded-lg",
                                    ),
                                ),
                                class_name="flex-1 h-48",
                            ),
                            rx.el.button(
                                rx.cond(
                                    TakeoffState.is_uploading,
                                    rx.el.span("Uploading..."),
                                    rx.el.span("Upload Selected Files"),
                                ),
                                on_click=[
                                    TakeoffState.handle_upload(
                                        rx.upload_files(upload_id=UPLOAD_ID)
                                    ),
                                    rx.clear_selected_files(UPLOAD_ID),
                                ],
                                class_name="mt-4 w-full bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 disabled:opacity-50",
                                disabled=TakeoffState.is_uploading
                                | (rx.selected_files(UPLOAD_ID).length() == 0),
                            ),
                            rx.cond(
                                TakeoffState.uploaded_files.length() > 0,
                                rx.el.button(
                                    "Clear All",
                                    on_click=TakeoffState.clear_uploads,
                                    class_name="mt-2 w-full bg-red-600 text-white px-6 py-2 rounded-lg hover:bg-red-700",
                                ),
                                rx.fragment(),
                            ),
                            class_name="flex-1 flex flex-col justify-between",
                        ),
                        rx.el.div(
                            rx.el.h3(
                                "Required Files:",
                                class_name="text-md font-semibold text-gray-300 mb-3",
                            ),
                            rx.el.div(
                                rx.icon(
                                    "square_check",
                                    class_name=rx.cond(
                                        TakeoffState.has_pdf,
                                        "text-green-500",
                                        "text-gray-500",
                                    ),
                                ),
                                rx.el.p(
                                    "At least 1 PDF Plan",
                                    class_name="text-gray-400 text-sm ml-2",
                                ),
                                class_name="flex items-center mb-6",
                            ),
                            rx.el.button(
                                "Generate Takeoff",
                                on_click=TakeoffState.generate_takeoff,
                                class_name="w-full bg-gray-600 text-white px-6 py-3 rounded-xl hover:bg-gray-500 transition-colors duration-200 font-semibold shadow-sm disabled:opacity-50 disabled:cursor-not-allowed",
                                disabled=~TakeoffState.has_pdf,
                            ),
                            class_name="flex-1 lg:ml-8 mt-8 lg:mt-0",
                        ),
                        class_name="grid grid-cols-1 lg:grid-cols-2 gap-8 items-start",
                    ),
                    class_name="bg-gray-800 p-8 rounded-2xl shadow-lg",
                ),
                class_name="container mx-auto px-4 sm:px-6 lg:px-8 py-12",
            ),
            class_name="flex-grow",
        ),
        footer_component(),
        class_name="font-['Roboto'] bg-gray-900 min-h-screen flex flex-col",
    )