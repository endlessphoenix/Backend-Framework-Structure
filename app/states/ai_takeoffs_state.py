import reflex as rx
import logging


class AITakeoffsState(rx.State):
    """State for the AI Takeoffs page."""

    uploaded_files: list[str] = []
    is_uploading: bool = False

    @rx.var
    def has_pdf(self) -> bool:
        """Check if at least one PDF file has been uploaded."""
        return any((f.lower().endswith(".pdf") for f in self.uploaded_files))

    @rx.event
    async def handle_upload(self, files: list[rx.UploadFile]):
        """Handle file uploads."""
        if not files:
            return rx.toast.error("No files selected.")
        self.is_uploading = True
        try:
            for file in files:
                upload_data = await file.read()
                output_path = rx.get_upload_dir() / file.name
                with output_path.open("wb") as f:
                    f.write(upload_data)
                self.uploaded_files.append(file.name)
            return rx.toast.success(f"Successfully uploaded {len(files)} file(s).")
        except Exception as e:
            logging.exception(f"Upload failed: {e}")
            return rx.toast.error("File upload failed.")
        finally:
            self.is_uploading = False

    @rx.event
    def generate_takeoff(self):
        """Placeholder for generating the takeoff."""
        if not self.has_pdf:
            return rx.toast.warning("At least one PDF file is required.")
        return rx.toast.info("Generating takeoff... (feature not implemented)")