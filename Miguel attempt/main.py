from datetime import date
import envelope
import payment


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
    name = input("Enter the name of new envelope: ")
    try:
        allocation = int(input(f"enter allocation for {name}: "))
        new_envelope = envelope.Envelope(name, allocation) #could be used for later
    except ValueError:
        print("Invalid allocation amount! Please enter amount.")
        
def create_payment():
    name = input("Enter the name of payment's Envelope: ")
    allocation = match_decimal(input(f"enter allocation for {name}: "))
    new_payment = payment.Payment(allocation, date.today(), False, False, name)    


total = envelope.Envelope("total", 5000)
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


