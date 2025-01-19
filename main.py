from datetime import date
import envelope
import payment


#Lets create a basic UI

def formatPayment(input):
    formattedInput = f"{input:.2f}"
    return formattedInput

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
    allocation = int(input(f"enter allocation for {name}: "))
    new_payment = payment.Payment(allocation, date.today(), False, False, name)
    new_payment.record()
    


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


