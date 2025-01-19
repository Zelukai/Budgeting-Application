from datetime import date
import envelope
import payment
import os


#Lets create a basic UI

def formatPayment(input):
    formattedInput = "{:.2f}".format(float(input))
    return formattedInput


def match_decimal(input_value):
    input_value = str(input_value)
    match input_value:
        case _ if '.' in input_value:
            before_decimal, after_decimal = input_value.split('.', 1)
            if len(after_decimal) > 2:
                print("Invalid input. More than two digits after the decimal.")
                input_value = input("Try again: ")
                return match_decimal(input_value)
            return formatPayment(input_value)
        case _:
            return formatPayment(input_value)            
            

def match_input(cLinput=3):
    match cLinput:
        case '1':
            create_envelope()
        case '2':
            create_payment()
        case '3':
            print("Thank you for using this Busy Budgeter! This program is now ending...")

def create_envelope():
    """Prompt the user to create a new envelope using depth-first recursion."""
    def ensure_parent_exists(parent_path):
        """Recursively ensure all parent folders exist."""
        if not os.path.exists(parent_path):
            # Get the grandparent path and ensure it exists first
            grandparent_path = os.path.dirname(parent_path)
            if grandparent_path and grandparent_path != "envelopes":
                ensure_parent_exists(grandparent_path)
            os.makedirs(parent_path, exist_ok=True)

    name = input("Enter the name of the new envelope: ").strip()
    try:
        allocation = int(input(f"Enter allocation for '{name}': "))
        if allocation <= 0:
            print("Allocation must be a positive number.")
            return

        # Check if the envelope is nested
        is_nested = input("Is this envelope nested inside another? (yes/no): ").strip().lower()
        if is_nested == "yes":
            parent_name = input("Enter the name of the parent envelope (e.g., Master/under): ").strip()
            
            # Build the parent folder path
            parent_folder = os.path.abspath(os.path.join("envelopes", *parent_name.split("/")))
            ensure_parent_exists(parent_folder)  # Ensure the parent folder exists

            # Build the path for the new envelope
            folder_path = os.path.join(parent_folder, name)
        else:
            # Create a root-level folder
            folder_path = os.path.abspath(os.path.join("envelopes", name))
            ensure_parent_exists(folder_path)  # Ensure the root folder exists

        # Create the new envelope's folder
        os.makedirs(folder_path, exist_ok=True)

        # Call the Envelope class to handle additional logic
        new_envelope = envelope.Envelope(name=name, allocation=allocation)

        print(f"Envelope '{name}' created successfully in '{folder_path}'.")
    except ValueError:
        print("Invalid allocation amount! Please enter a valid integer.")


def create_payment():
    name = input("Enter the name of payment's Envelope: ")
    allocation = match_decimal(input(f"enter allocation for {name}: "))
    new_payment = payment.Payment(allocation, date.today(), False, False, name)    


def main():
    print("Welcome to the Busy Budgeter")
    print("What would you like to do? \n 1. Create an budgeting envelope \n 2. Enter a new payment \n 3. Exit Program")
    cLinput = input()
    while cLinput not in ('1', '2', '3'):
        print("Invalid option! Please enter a valid option (1, 2, or 3)")
        cLinput = input()
    match_input(cLinput)


if __name__ == "__main__":
    main()


