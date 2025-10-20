import reflex as rx
import os


class TakeoffState(rx.State):
    """State for the AI Takeoffs page."""

    uploaded_files: list[str] = []
    is_uploading: bool = False

    @rx.event
    async def handle_upload(self, files: list[rx.UploadFile]):
        """Handles the file upload."""
        self.is_uploading = True
        try:
            for file in files:
                upload_data = await file.read()
                outfile = rx.get_upload_dir() / file.name
                with outfile.open("wb") as f:
                    f.write(upload_data)
                self.uploaded_files.append(file.name)
        finally:
            self.is_uploading = False

    @rx.event
    def clear_uploads(self):
        """Clears the uploaded files."""
        self.uploaded_files = []