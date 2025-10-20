import reflex as rx
from app.states.takeoff_state import TakeoffState
from app.components.header import header_component
from app.components.footer import footer_component


def uploaded_file_item(filename: str) -> rx.Component:
    return rx.el.div(
        rx.el.p(filename, class_name="text-sm font-medium text-gray-300"),
        class_name="flex items-center justify-between p-3 bg-gray-700 rounded-lg",
    )


def takeoffs_page() -> rx.Component:
    """The AI Takeoffs page with file upload functionality."""
    return rx.el.div(
        header_component(),
        rx.el.main(
            rx.el.div(
                rx.el.h1(
                    "AI Takeoffs", class_name="text-4xl font-extrabold text-white mb-2"
                ),
                rx.el.p(
                    "Upload your construction plans or blueprints to get started.",
                    class_name="text-lg text-gray-400 mb-8",
                ),
                rx.el.div(
                    rx.upload.root(
                        rx.el.div(
                            rx.icon(
                                "cloud_upload",
                                class_name="w-12 h-12 mx-auto text-gray-500",
                            ),
                            rx.el.p(
                                "Drag & drop files here, or click to select files",
                                class_name="text-center text-gray-400 mt-4",
                            ),
                            class_name="flex flex-col items-center justify-center w-full h-full p-8",
                        ),
                        id="upload_area",
                        class_name="w-full h-64 border-2 border-dashed border-gray-600 rounded-xl cursor-pointer bg-gray-800/50 hover:bg-gray-800/80 transition-colors",
                    ),
                    rx.el.div(
                        rx.el.button(
                            "Upload",
                            on_click=TakeoffState.handle_upload(
                                rx.upload_files(upload_id="upload_area")
                            ),
                            class_name="bg-blue-600 text-white px-6 py-2 rounded-xl hover:bg-blue-700 transition-colors duration-200 font-semibold disabled:opacity-50 disabled:cursor-not-allowed",
                            disabled=TakeoffState.is_uploading,
                        ),
                        rx.el.button(
                            "Clear Selected",
                            on_click=rx.clear_selected_files("upload_area"),
                            class_name="bg-gray-600 text-white px-6 py-2 rounded-xl hover:bg-gray-500 transition-colors duration-200 font-semibold",
                        ),
                        class_name="flex gap-4 mt-4",
                    ),
                    rx.el.div(
                        rx.el.h3(
                            "Selected Files",
                            class_name="text-xl font-semibold text-white mb-4",
                        ),
                        rx.foreach(
                            rx.selected_files("upload_area"),
                            lambda file: rx.el.p(file, class_name="text-gray-300"),
                        ),
                        class_name="mt-8",
                    ),
                    rx.cond(
                        TakeoffState.uploaded_files.length() > 0,
                        rx.el.div(
                            rx.el.div(
                                rx.el.h3(
                                    "Uploaded Files",
                                    class_name="text-xl font-semibold text-white",
                                ),
                                rx.el.button(
                                    "Clear Uploads",
                                    on_click=TakeoffState.clear_uploads,
                                    class_name="bg-red-600 text-white px-4 py-2 rounded-xl hover:bg-red-700 transition-colors text-sm font-semibold",
                                ),
                                class_name="flex justify-between items-center mb-4",
                            ),
                            rx.el.div(
                                rx.foreach(
                                    TakeoffState.uploaded_files, uploaded_file_item
                                ),
                                class_name="space-y-3",
                            ),
                            class_name="mt-8",
                        ),
                        rx.fragment(),
                    ),
                    class_name="max-w-3xl mx-auto",
                ),
                class_name="container mx-auto px-4 sm:px-6 lg:px-8 py-12",
            ),
            class_name="flex-grow",
        ),
        footer_component(),
        class_name="font-['Roboto'] bg-gray-900 min-h-screen flex flex-col",
    )