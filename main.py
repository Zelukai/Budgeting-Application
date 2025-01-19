import pandas
import datetime
import envelope


#Lets create a basic UI

total = envelope.Envelope("total", 5000)
def main():
    while True:
        print("Welcome to the Busy Budgeter")
        print("What would you like to do? \n 1. Create an budgeting envelope \n 2. Enter a new payment \n 3. Exit Program")
        cLinput = input()
        while (cLinput != 1 or cLinput != 2 or cLinput != 3):
            print("Invalid option! Please enter a valid option (1, 2, or 3)")
            cLinput = input()
        break

if __name__ == "__main__":
    main()