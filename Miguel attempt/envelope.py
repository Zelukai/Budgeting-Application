import csv
from datetime import date
import os 

class Envelope:
    envelope_names = []

    def __init__(self, name, allocation, parent=None):
        self.name = name
        self.allocation = allocation
        self.parent = parent
        self.children = []

        # Build the folder path
        self.folder_path = self.build_folder_path()
        os.makedirs(self.folder_path, exist_ok=True)

        # Add to parent if applicable
        if parent:
            parent.add_child(self)

        # Register the envelope
        Envelope.envelope_names.append(self)

        # Automatically record to CSV
        self.record()

    def build_folder_path(self):
        """Build the folder path for the envelope."""
        if self.parent:
            return os.path.join(self.parent.folder_path, self.name)
        return os.path.join("envelopes", self.name)

    def add_child(self, child):
        """Add a child envelope."""
        self.children.append(child)

    def record(self):
        """Write envelope details to a CSV file."""
        csv_file_path = os.path.join(self.folder_path, f"{self.name}.csv")
        headers = ["Amount", "Date", "Envelope"]

        file_exists = os.path.exists(csv_file_path)
        with open(csv_file_path, mode="a" if file_exists else "w", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(headers)  # Write headers only if new
            writer.writerow([self.allocation, date.today(), self.folder_path])

        print(f"Envelope '{self.name}' created successfully in '{self.folder_path}'.")

    @classmethod
    def load_envelopes_from_filesystem(cls, base_dir="envelopes"):
        """Scan the envelopes directory and rebuild the envelope names list."""
        cls.envelope_names = []
        for root, dirs, files in os.walk(base_dir):
            for dir_name in dirs:
                # Add each folder as an Envelope name
                cls.envelope_names.append(dir_name)
