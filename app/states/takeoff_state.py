import reflex as rx
import logging


class TakeoffState(rx.State):
    """State for the AI Takeoffs page."""

    uploaded_files: list[str] = []
    is_uploading: bool = False

    @rx.var
    def has_pdf(self) -> bool:
        """Check if at least one PDF file has been uploaded."""
        for file_name in self.uploaded_files:
            if file_name.lower().endswith(".pdf"):
                return True
        return False

    @rx.event
    async def handle_upload(self, files: list[rx.UploadFile]):
        """Handles the file upload process."""
        if not files:
            return
        self.is_uploading = True
        yield
        for file in files:
            upload_data = await file.read()
            self.uploaded_files.append(file.name)
        self.is_uploading = False
        yield

    @rx.event
    def generate_takeoff(self):
        """Placeholder for generating the takeoff."""
        logging.info("Generating takeoff with files:", self.uploaded_files)
        yield rx.toast("Takeoff generation started!")

    @rx.event
    def clear_uploads(self):
        """Clears the uploaded files."""
        self.uploaded_files = []