import os
import csv
from envelope import Envelope
from datetime import date

def create_envelope():
    """Prompt the user to create a new envelope."""
    name = input("Enter the name of the new envelope: ").strip()
    try:
        allocation = int(input(f"Enter allocation for '{name}': "))
        if allocation <= 0:
            print("Allocation must be a positive number.")
            return

        # Ask if this envelope is nested
        is_nested = input("Is this envelope nested inside another? (yes/no): ").strip().lower()
        parent_envelope = None

        if is_nested == "yes":
            parent_name = input("Enter the name of the parent envelope: ").strip()

            # Locate the parent envelope
            for env in Envelope.envelope_names:
                if env.name == parent_name:
                    parent_envelope = env
                    break

            if not parent_envelope:
                print(f"Parent envelope '{parent_name}' not found. Please create it first.")
                return

        # Create the envelope
        Envelope(name=name, allocation=allocation, parent=parent_envelope)

    except ValueError:
        print("Invalid allocation amount! Please enter a valid integer.")


def update_csv_files_deepest_first(base_dir="envelopes"):
    """Merge CSV data starting from the deepest folders."""
    all_folders = []
    for root, dirs, files in os.walk(base_dir):
        all_folders.append(root)

    # Sort folders by depth (deepest first)
    all_folders.sort(key=lambda path: path.count(os.sep), reverse=True)

    for folder in all_folders:
        csv_files = [f for f in os.listdir(folder) if f.endswith('.csv')]
        combined_data = []

        # Read and combine CSV data
        for csv_file in csv_files:
            file_path = os.path.join(folder, csv_file)
            with open(file_path, mode="r") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                combined_data.extend(list(reader))

        # Save the combined data back to each CSV file
        for csv_file in csv_files:
            file_path = os.path.join(folder, csv_file)
            with open(file_path, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Amount", "Date", "Envelope"])
                writer.writerows(combined_data)

def main():
    """Main program loop."""
    while True:
        print("\nWhat would you like to do?")
        print("1. Create a budgeting envelope")
        print("2. Merge CSV files")
        print("3. Exit")
        choice = input("> ").strip()

        if choice == "1":
            create_envelope()
        elif choice == "2":
            update_csv_files_deepest_first()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()