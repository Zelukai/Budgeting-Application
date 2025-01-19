from datetime import date
import envelope
import payment
import pandas as pd
import os

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

def match_input(cLinput=3):
    match cLinput:
        case '1':
            create_envelope()
            base_directory = "envelopes"
        case '2':
            create_payment()
        case '3':
            print("Thank you for using this Busy Budgeter! This program is now ending...")

def create_envelope():
    name = input("Enter the name of the new envelope: ").strip()
    allocation = int(input(f"Enter allocation for '{name}': "))
    
    is_nested = input("Is this envelope inside another? (Y/N): ").strip().lower()
    if is_nested == "y":
        parent_name = input("Enter the name of the parent envelope: ").strip()
        print(find(parent_name))
        envelope.Envelope(name=name, allocation=allocation, parent=parent_name)
    else:
        envelope.Envelope(name=name, allocation=allocation)

def create_payment():
    amount = match_decimal(input("Enter payment amount: "))
    envelope = input("Enter the name of payment's Envelope: ")
    
    payment.Payment(envelope=envelope, amount=amount)   

def main():
    print("Welcome to your Busy Budgeter !")
    print("What would you like to do? \n 1. Create a budgeting envelope \n 2. Enter a new payment \n 3. Exit Program")
    cLinput = input()
    while cLinput not in ('1', '2', '3'):
        print("Invalid option! Please enter a valid option (1, 2, or 3)")
        cLinput = input()
    match_input(cLinput)


if __name__ == "__main__":
    main()


