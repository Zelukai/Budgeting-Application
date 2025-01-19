import csv
import datetime
import payment
from datetime import date
import os 

class Envelope:
    envelope_names = []

    def __init__(self, name: str, allocation: int, parent=None, children=None):
        self.name = name
        self.parent = parent
        self.allocation = allocation
        self.children = children or []  # Avoid mutable default arguments
        self.exp_running_t = allocation  # Initialize remaining allocation

        # Determine the folder path
        if parent:
            # Check if the parent exists
            if parent not in Envelope.envelope_names:
                raise ValueError(f"Parent envelope '{parent}' does not exist.")
            # Create the nested folder path
            self.folder_path = os.path.join("envelopes", parent, self.name)
        else:
            # Root folder for top-level envelope
            self.folder_path = os.path.join("envelopes", self.name)

        # Ensure the folder structure exists
        os.makedirs(self.folder_path, exist_ok=True)

        # Add this envelope's name to the global list
        Envelope.envelope_names.append(self.name)

        # Automatically record the envelope's details in a CSV
        self.record()

    def add_child(self, child):
        """Add a child envelope to this envelope."""
        self.children.append(child)

    def record(self):
        """Record envelope details in a CSV file."""
        # Define the CSV file path
        csv_file_path = os.path.join(self.folder_path, f"{self.name}.csv")

        # List of CSV headers
        headersList = ["Amount","Date","Envelope"]

        # Write to the CSV file
        file_exists = os.path.exists(csv_file_path)
        with open(csv_file_path, mode="a" if file_exists else "w", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(headersList)  # Write headers only if the file is new
            writer.writerow([
            self.allocation,  # Amount
            date.today(),     # Date
            self.folder_path  # Folder path (Envelope)
        ])

        # Display user feedback
        print(f"Envelope '{self.name}' was created in '{self.folder_path}'.")
        print(f"Funds allocated: {self.allocation}")
    