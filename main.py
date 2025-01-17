from datetime import date
import envelope
import payment
import pandas as pd
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

def find(folder_name):
    # find filepath of folder with input name
    for root, dirs, files in os.walk('envelopes'):
        if folder_name in dirs:
            return os.path.join(root, folder_name)
    return None

# def update_csv_files_deepest_first(base_dir):
#     # Get all folder paths
#     all_folders = []
#     for root, dirs, files in os.walk(base_dir):
#         all_folders.append(root)
    
#     # Sort folders by depth (deepest folders first)
#     all_folders.sort(key=lambda path: path.count(os.sep), reverse=True)
    
#     # Dictionary to store combined data for each folder
#     folder_data = {}

#     # Process folders starting from the deepest
#     for folder in all_folders:
#         csv_files = [f for f in os.listdir(folder) if f.endswith('.csv')]
        
#         # Read data from CSV files in the current folder
#         dataframes = []
#         for csv_file in csv_files:
#             file_path = os.path.join(folder, csv_file)
#             df = pd.read_csv(file_path)
#             dataframes.append(df)
        
#         # Combine data from this folder
#         combined_df = pd.concat(dataframes, ignore_index=True) if dataframes else pd.DataFrame()
        
#         # Add data from child folders (if any) to this folder's combined data
#         child_folders = [f for f in os.listdir(folder) if os.path.isdir(os.path.join(folder, f))]
#         for child_folder in child_folders:
#             child_path = os.path.join(folder, child_folder)
#             if child_path in folder_data:
#                 combined_df = pd.concat([combined_df, folder_data[child_path]], ignore_index=True)
        
#         # Save combined data back to CSV files in the current folder
#         for csv_file in csv_files:
#             file_path = os.path.join(folder, csv_file)
#             combined_df.to_csv(file_path, index=False)
        
#         # Store the combined data for this folder for use by parent folders
#         folder_data[folder] = combined_df
       
            


def match_input(cLinput=3):
    match cLinput:
        case '1':
            create_envelope()
            base_directory = "envelopes"
            #update_csv_files_deepest_first(base_directory)
        case '2':
            create_payment()
        case '3':
            print("Thank you for using this Busy Budgeter! This program is now ending...")

def create_envelope():
    name = input("Enter the name of the new envelope: ").strip()
    allocation = int(input(f"Enter allocation for '{name}': "))
    
    is_nested = input("Is this envelope nested inside another? (Y/N): ").strip().lower()
    if is_nested == "y":
        parent_name = input("Enter the name of the parent envelope: ").strip()
        print(find(parent_name))
        envelope.Envelope(name=name, allocation=allocation, parent=parent_name)
    else:
        envelope.Envelope(name=name, allocation=allocation)





# def create_envelope():
#     """Prompt the user to create a new envelope."""
#     name = input("Enter the name of the new envelope: ").strip()
#     try:
#         allocation = int(input(f"Enter allocation for '{name}': "))
#         if allocation <= 0:
#             print("Allocation must be a positive number.")
#             return

#         # Ask if this envelope is nested
#         is_nested = input("Is this envelope nested inside another? (yes/no): ").strip().lower()
#         parent_envelope = None

#         if is_nested == "yes":
#             parent_name = input("Enter the name of the parent envelope: ").strip()

#             # Locate the parent envelope
#             for env in envelope.Envelope.envelope_names:
#                 if env.name == parent_name:
#                     parent_envelope = env
#                     break

#             if not parent_envelope:
#                 print(f"Parent envelope '{parent_name}' not found. Please create it first.")
#                 return

#         # Create the envelope
#         envelope.Envelope(name=name, allocation=allocation, parent=parent_envelope)

#     except ValueError:
#         print("Invalid allocation amount! Please enter a valid integer.")

        
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


